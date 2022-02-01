import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp
import datetime

import matplotlib as plt
import seaborn as sns
from seaborn.matrix import heatmap


def create_labels(date_code, current_labels, date_list):
    tick_number = len(current_labels)
    interval = int(len(date_list) / tick_number)

    return [date_list[i].strftime(date_code) for i in range(
        0, (interval * tick_number), interval)]


# organize data

df = pd.read_csv("WeatherData.csv")
datetimes = pd.to_datetime(df["datetime"])

times = [datetimes[i].time() for i in range(0, len(datetimes))]
dates = [datetimes[i].date() for i in range(0, len(datetimes))]
df["times"] = times
df["dates"] = dates


def create_heatmap(data, title):
    pdf = pd.pivot_table(df, values=[data],
                         index=df["dates"], columns=["times"])

    heatmap = sns.heatmap(
        pdf, square=False)

    # create and set heatmap appearance

    heatmap.set_title(data + " " + title)
    heatmap.set_xticklabels(create_labels(
        "%H", heatmap.get_xticklabels(), times[:24]))

    heatmap.set_yticklabels(create_labels(
        "%m %d, %Y", heatmap.get_yticklabels(), dates))

    heatmap.set_xlabel("Time (h)")


create_heatmap(
    "humidity", "in Andover, as a function of the date and time")
plt.pyplot.show()
