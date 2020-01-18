import pandas as pd
import plotly.graph_objects as go
import plotly

# read data
df = pd.read_csv('/Users/tomgurrie/sankey_austin.csv')

# convert to dictionary
data = df[['source','target','value']].to_dict(orient="list")

# create plot
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Aus-E", "Aus-W", "Both", "New", "Aus-E", "Aus-W", "Both", "Lapsed"],
      color = "blue"
    ),
    link = data
  )])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)

plotly.offline.plot(fig, filename='sankey_austin.html')

