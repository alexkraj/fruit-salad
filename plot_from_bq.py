import json
import os

from os import listdir
from os.path import isfile, join

import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

csv_name=""

# read csv into pandas
df = pd.read_csv(csv_name)
# convert col into datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])
# remove timezone to allow for conversion to epoch
df['timestamp'] = df['timestamp'].dt.tz_localize(None)
df['timestamp']=(df['timestamp'] - dt.datetime(1970,1,1)).dt.total_seconds()
# plots all columns against index
# scatter plot
df.plot() 
df.plot(kind='scatter',x='timestamp',y='x_horizon_request_duration') 
plt.show()