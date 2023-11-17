import json
import plotly.express as px
import pandas as pd
import sys

df = pd.read_json("cycletrackingjsonAllEscape.json")
for i in range(10):
    # Gather
    ##########################
    gather = df.get("pattern")[i]
    print(f"Gather {i}, Pattern length:" +  len(df.get("pattern")[i]))
    gather = gather[0:1000]

    #Gather Histogram
    fig = px.histogram(x=gather, 
    title="Quicksilver AllEscape, Histogram func=CycleTrackingFunction, Gather",
    log_y=True).update_layout(yaxis_title="count", xaxis_title="pattern[i]")
    fig.write_html(f"gather_histograms/Gather{i}_histogram.html")

    #Gather Bandwidth
    fig = px.scatter(y=gather, 
    title="Quicksilver AllEscape, Bandwidth func=CycleTrackingFunction, Gather", log_y=True, log_x=True).update_layout(xaxis_title="i", yaxis_title="pattern[i]")
    fig.write_html(f"gather_bandwidth/Gather{i}_Bandwidth.html")

    #Gather delta
    gather_delta = [0] * len(gather)
    for j in range(1, len(gather)):
        gather_delta[j] = gather[j] - gather[j-1]
    fig = px.scatter(y=gather_delta, 
    title="Quicksilver AllEscape, Deltas func=CycleTrackingFunction, Gather", log_x=True).update_layout(xaxis_title="time", yaxis_title="delta")
    fig.write_html(f"gather_deltas/Gather{i}_deltas.html")

    #Gather delta histogram
    fig = px.histogram(x=gather_delta,
    title="Quicksilver AllEscape, Deltas Histogram func=CycleTrackingFunction, Gather",
    log_y=True).update_layout(yaxis_title="count", xaxis_title="delta")
    fig.write_html(f"gather_deltas_histograms/Gather{i}_delta_histogram.html")
    
    
    #Scatter
    ################################
    scatter = df.get("pattern")[i+10]
    print(f"Scatter {i}, Pattern length:" +  len(df.get("pattern")[i+10]))
    
    #Scatter histogram
    fig = px.histogram(x=scatter, 
    title="Quicksilver AllEscape, Histogram func=CycleTrackingFunction, Scatter"
    ).update_layout(yaxis_title="count", xaxis_title="pattern[i]")
    fig.write_html(f"scatter_histograms/Scatter{i}_Hist_count_as_y.html")

    #Scatter bandwidth
    fig = px.scatter(y=scatter, 
    title="Quicksilver AllEscape, Bandwidth func=CycleTrackingFunction, Scatter").update_layout(xaxis_title="i", yaxis_title="pattern[i]")
    fig.write_html(f"scatter_bandwidth/Scatter{i}_bandwidth.html")

    #Scatter delta
    scatter_delta = [0] * len(scatter)
    for j in range(1, len(scatter)):
        scatter_delta[j] = scatter[j] - scatter[j-1]
    fig = px.scatter(y=scatter_delta, 
    title="Quicksilver AllEscape, Deltas func=CycleTrackingFunction, Scatter", log_x=True).update_layout(xaxis_title="time", yaxis_title="delta")
    fig.write_html(f"scatter_deltas/Scatter{i}_deltas.html")

    #Gather delta histogram
    fig = px.histogram(x=scatter_delta,
    title="Quicksilver AllEscape, Deltas Histogram func=CycleTrackingFunction, Scatter",
    log_y=True).update_layout(yaxis_title="count", xaxis_title="delta")
    fig.write_html(f"scatter_deltas_histograms/Scatter{i}_delta_histogram.html")