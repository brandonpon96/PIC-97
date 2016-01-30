# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 08:17:35 2016

@author: Matt
"""

import pandas as pd
import os                  # has function for getting filenames in directory
from pytz import timezone  # used to identify timezones

nearest = 1e3*60*20        # 20 minutes expressed in milliseconds

# the directory of all the data
pwd = r"C:\Users\Matt\Dropbox (Personal)\UCLA\Teaching\PIC 97\Lecture\Lecture 9\2013"

# loads a single CSV file and processes it
def process_file(file):
    x = pd.read_csv(pwd+"\\"+file, names = ["Time", "Inst", "Cumu"]) # load from excel and add column names         
    x = x[x.Inst.notnull()]                                          # remove NaNs (Not a Numbers)
    x.iloc[0,0] = round_time(x.iloc[0,0],nearest)                    # round the first timestamp down to the nearest 20min
    x.set_index("Time",inplace = True)                               # make the time column the index
    x.index = pd.to_datetime(x.index, unit = "ms", utc = True)       # convert the timestamps to DateTimes and make them timezone aware (UTC)
    x =  x.tz_convert(timezone("US/Eastern"))                        # convert the DateTimes to Eastern time
    x = x.asfreq('20Min', method='pad')                              # interpolate at 20min intervals
    x["TOD"] = x.index.strftime("%A-%H-%M")                          # wreate a new "Time of Day" column with Day of Week - Hour - Minute
    return x

def round_time(time, nearest):
    return int(time/nearest) * nearest                               

files = os.listdir(pwd)           # get all filenames
file = files[0];
files = files[1:];
df = process_file(file)
for i,file in enumerate(files): 
    if file.endswith("csv"):
        x = process_file(file)
        df = pd.concat([df,x])   # concatenate all processed data to single DataFrame

grouped = df.groupby("TOD")                            # group rows by TOD
final = grouped.agg({"Inst": pd.Series.mean})          # calculate means of groups
final.to_excel("output.xlsx",sheet_name = "Worksheet") # save results