import json
import plotly.express as px
import pandas as pd
import sys

df = pd.read_json("cycletrackingjsonAllScattering.json")

gather = df.get("pattern")[0]
fig = px.histogram(y=gather, 
title="Quicksilver, Histogram func=CycleTrackingFunction, Gather",
log_x=True).update_layout(xaxis_title="count", yaxis_title="accessed cache block index")
fig.update_yaxes(range=[0,150])
fig.write_image("Gather_count_as_x.png")

gather = df.get("pattern")[0]
fig = px.histogram(x=gather, 
title="Quicksilver, Histogram func=CycleTrackingFunction, Gather",
log_y=True).update_layout(yaxis_title="count", xaxis_title="accessed cache block index")
fig.update_xaxes(range=[0,150])
fig.write_image("Gather_count_as_y.png")

# gather = df.get("pattern")[0]
# fig = px.scatter(y=gather, 
# title="Quicksilver, Bandwidth func=CycleTrackingFunction, Gather").update_layout(xaxis_title="index/time", yaxis_title="accessed cache block index")
# fig.update_xaxes(range=[0,50])
# fig.write_image("Gather_bandwidth.png")

# scatter = df.get("pattern")[12]
# fig = px.histogram(y=scatter, 
# title="Quicksilver, Histogram func=CycleTracking, Scatter",
# log_x=True).update_layout(xaxis_title="count", yaxis_title="accessed cache block index")
# fig.update_yaxes(range=[0,5])
# fig.write_image("Scatter_Hist_count_as_x.png")

# scatter = df.get("pattern")[12]
# fig = px.histogram(x=scatter, 
# title="Quicksilver, Histogram func=CycleTracking, Scatter",
# log_y=True).update_layout(yaxis_title="count", xaxis_title="accessed cache block index")
# fig.update_xaxes(range=[0,5])
# fig.write_image("Scatter_Hist_count_as_y.png")

# scatter = df.get("pattern")[12]
# fig = px.scatter(y=scatter, 
# title="Quicksilver, Bandwidth func=CycleTracking, Gather").update_layout(xaxis_title="index/time", yaxis_title="accessed cache block index")
# fig.update_xaxes(range=[0,50])
# fig.write_image("Scatter_bandwidth.png")