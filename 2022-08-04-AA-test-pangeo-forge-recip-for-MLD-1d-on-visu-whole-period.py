#!/usr/bin/env python

import pandas as pd
import xarray as xr

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern
from pangeo_forge_recipes.recipes import XarrayZarrRecipe,setup_logging


dates = pd.date_range('2009-07-01', '2010-06-30', freq='D')


dates

URL_FORMAT = (
    "https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/fileServer/meomopendap/extract/"
    "eNATL60/eNATL60-BLBT02/1d/eNATL60-BLBT02_y{time:%Y}m{time:%m}d{time:%d}.1d_somxl010.nc"
)

def make_url(time):
    return URL_FORMAT.format(time=time)


truc=make_url(dates[0])

time_concat_dim = ConcatDim("time", dates, nitems_per_file=1)
time_concat_dim

pattern = FilePattern(make_url, time_concat_dim)
pattern

for index, url in pattern.items():
    print(index)
    print(url)
    # Stop after the 3rd filepath (September 3rd, 1981)
    if 'y2009m07d05' in url:
        break

target_chunks = {"time_counter": 1, "y": 1500}
recipe = XarrayZarrRecipe(pattern, target_chunks=target_chunks)
recipe


setup_logging()


recipe.file_pattern

run_function = recipe.to_function()

run_function()

mld_zarr_prune = xr.open_zarr(recipe.target_mapper, consolidated=True)
mld_zarr_prune




