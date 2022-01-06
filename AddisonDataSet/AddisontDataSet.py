import matplotlib as plt

from pandas._libs.tslibs import timedeltas
import seaborn as sns
import pandas as pd

import numpy as np
import datetime


cmap = plt.pyplot.get_cmap("Oranges")
cmap_r = plt.pyplot.get_cmap("Oranges_r")

df = pd.read_csv(
    "/Users/brianmasse/Developer/Python/CSC630/CSC630/AddisonDataSet/AddisoDataSet.csv")

dates = pd.to_datetime(df["Date"])
times = df["Time (h)"]
df["Date"] = dates

hd = pd.pivot_table(df, columns=[
    "Time (h)"], index=["Date"], values=["Humidity"], fill_value=0)
td = pd.pivot_table(df, columns=[
    "Time (h)"], index=["Date"], values=["Temperature"], fill_value=0)

# humidtyHeatMap = sns.heatmap(
#     hd, vmin=40, square=False, cmap=cmap)

tempHeatMap = sns.heatmap(
    td, vmin=65, square=False, cmap=cmap_r)


tick_number = len(tempHeatMap.get_yticklabels())
interval = int(len(dates) / tick_number)
y_labels = [dates[i].strftime("%m-%d-%y")
            for i in range(0, (interval * tick_number), interval)]

x_labels = [datetime.datetime.strptime(str(times[i]), "%H:%M:%S").strftime("%H")
            for i in range(0, (24))]

# humidtyHeatMap.set_xticklabels(x_labels, rotation=65)
# humidtyHeatMap.set_yticklabels(y_labels)
tempHeatMap.set_xticklabels(x_labels, rotation=65)
tempHeatMap.set_yticklabels(y_labels)

# humidtyHeatMap.set_ylabel("Dates, through Sep 2020 to Sep 2021")
# humidtyHeatMap.set_xlabel("Time, in hours")
# humidtyHeatMap.set_title(
#     "The Humidity in the addision at certain times and dates")
tempHeatMap.set_ylabel("Dates, through Sep 2020 to Sep 2021")
tempHeatMap.set_xlabel("Time, in hours")
tempHeatMap.set_title(
    "The Temperature in the addision at certain times and dates")


plt.pyplot.show()
