import plotly.graph_objects as go
import numpy as np

# Load data
chunk = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_UNVX.csv", comments='#', delimiter=',', skiprows=1)
DATA = np.array(chunk)
Ys = DATA[:, 0]
Xs = DATA[:, 1]

# Create 2D histogram plot
fig = go.Figure(data=[go.Histogram2d(
    x=Xs,
    y=Ys,
    colorscale='Viridis'
)])

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Count'
    ),
    width=800,
    height=800
)

# Export to HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_Histogram_Y_UNVX.html")

# Show plot
fig.show()