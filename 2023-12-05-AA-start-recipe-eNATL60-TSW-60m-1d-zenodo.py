import pandas as pd
import xarray as xr

from pangeo_forge_recipes.patterns import ConcatDim, FilePattern, MergeDim

dates = pd.date_range('2009-07-01', '2010-06-30', freq='D')

records = {
    1:'10261988',
    2:'10260907',
    3:'10260980',
    4:'10261078',
    5:'10261126',
    6:'10261192',
    7:'10261274',
    8:'10261349',
    9:'10261461',
    10:'10261540',
    11:'10262356',
    12:'10261643'
}

def make_full_path(time):
    record=str(records[time.month])
    date='y'+str(time.year)+'m'+str("{:02d}".format(time.month))+'d'+str("{:02d}".format(time.day))
    return f"https://zenodo.org/records/{record}/files/eNATL60-BLBT02_{date}.1d_TSW_60m.nc"

time_concat_dim = ConcatDim("time", dates, nitems_per_file=1)
pattern = FilePattern(make_full_path, time_concat_dim)
