import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as pgo

#  full student graph  #

df = pd.read_csv("project csv's\p107-1.csv")
print(df.groupby("level")["attempt"].mean())

figure = pgo.Figure(pgo.Scatter(
x = df.groupby("level")["attempt"].mean(),
y = ["level 1","level 2","level 3","level 4"],
orientation = "h"
))
figure.show()
