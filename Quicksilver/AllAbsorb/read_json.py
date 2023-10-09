import json
import plotly.express as px
import pandas as pd
import sys

df = pd.read_json("CollisionEventjsonAllAbsorb.json")

for i in range(10):
    # Gather
    ##########################
    gather = df.get("pattern")[i]

    fig = px.histogram(x=gather, 
    title="Quicksilver, Histogram func=CollisionEvent, Gather",
    log_y=True).update_layout(yaxis_title="count", xaxis_title="index")
    fig.write_html(f"gather_histograms/Gather{i}_count_as_y.html")

    fig = px.scatter(y=gather, 
    title="Quicksilver, Bandwidth func=CollisionEvent, Gather", log_y=True, log_x=True).update_layout(xaxis_title="i", yaxis_title="pattern[i]")
    fig.write_html(f"gather_bandwidth/Gather{i}_Bandwidth.html")

    gather_delta = [0] * len(gather)
    for j in range(1, len(gather)):
        gather_delta[j] = gather[j] - gather[j-1]
    fig = px.scatter(y=gather_delta, 
    title="Quicksilver, Deltas func=CollisionEvent, Gather", log_x=True).update_layout(xaxis_title="time", yaxis_title="delta")
    fig.write_html(f"gather_deltas/Gather{i}_deltas.html")
    
    #Scatter
    ################################

    scatter = df.get("pattern")[i+10]
    
    fig = px.histogram(x=scatter, 
    title="Quicksilver, Histogram func=CollisionEvent, Scatter"
    ).update_layout(yaxis_title="count", xaxis_title="index")
    fig.write_html(f"scatter_histograms/Scatter{i}_Hist_count_as_y.html")

    fig = px.scatter(y=scatter, 
    title="Quicksilver, Bandwidth func=CollisionEvent, Scatter").update_layout(xaxis_title="i", yaxis_title="pattern[i]")
    fig.write_html(f"scatter_bandwidth/Scatter{i}_bandwidth.html")

    scatter_delta = [0] * len(scatter)
    for j in range(1, len(scatter)):
        scatter_delta[j] = scatter[j] - scatter[j-1]
    fig = px.scatter(y=scatter_delta, 
    title="Quicksilver, Deltas func=CollisionEvent, Scatter", log_x=True).update_layout(xaxis_title="time", yaxis_title="delta")
    fig.write_html(f"scatter_deltas/Scatter{i}_deltas.html")