import matplotlib as plt
import seaborn as sns

import pandas as pd


df = pd.read_csv(
    "/Users/brianmasse/Developer/Python/CSC630/CSC630/AddisonDataSet/AddisoDataSet.csv")

# dates = pd.to_datetime(df["Date"])
# times = df["Time (h)"]
# df["Date"] = dates

humPlot = sns.regplot(x=df["Date"], y=df["Humidity"], fit_reg=False,
                      scatter_kws={"alpha": 0.8, "s": 1})

tempPlot = sns.regplot(x=df["Date"], y=df["Temperature"], fit_reg=False,
                       scatter_kws={"alpha": 0.8, "s": 1})

# humPlot.set_xticklabels(humPlot.get_xticklabels)

plt.pyplot.show()
