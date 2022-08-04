import pandas as pd
import xarray as xr

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern
from pangeo_forge_recipes.recipes import XarrayZarrRecipe,setup_logging

dates = pd.date_range('2009-07-01', '2010-06-31', freq='D')

URL_FORMAT = (
    "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/"
    "eNATL60/eNATL60-BLBT02/1d/eNATL60-BLBT02_y{time:%Y}m{time:%m}d{time:%d}.1d_somxl010.nc"
)

def make_url(time):
    return URL_FORMAT.format(time=time)

time_concat_dim = ConcatDim("time", dates, nitems_per_file=24)
pattern = FilePattern(make_url, time_concat_dim)

recipe = XarrayZarrRecipe(pattern, inputs_per_chunk=2)

# Set up logging
setup_logging()

# Prune the recipe
recipe_pruned = recipe.copy_pruned()

# Run the recipe
run_function = recipe_pruned.to_function()
run_function()

# Check the output
mld_zarr = xr.open_zarr(recipe.target_mapper, consolidated=True)
mld_zarr
