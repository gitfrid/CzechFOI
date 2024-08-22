import plotly.graph_objects as go
import numpy as np

# Load data
chunk = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_VX_UNVX.csv", comments='#', delimiter=',', skiprows=1)
DATA = np.array(chunk)
Ys = DATA[:, 0]
Xs = DATA[:, 1]
Zs = DATA[:, 2]

# Create histogram
hist, xedges, yedges = np.histogram2d(Xs, Ys, bins=20)

# Construct arrays for the anchor positions of the bars
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

# Construct arrays with the dimensions for the bars
dx = dy = np.diff(xedges)[0]
dz = hist.ravel()

# Create the 3D surface plot
fig = go.Figure(data=[go.Surface(
    x=xpos.reshape((20, 20)),
    y=ypos.reshape((20, 20)),
    z=dz.reshape((20, 20)),
    colorscale='HSV',
    colorbar=dict(title='Count')
)])

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Count',
        xaxis=dict(nticks=20),
        yaxis=dict(nticks=6),
        zaxis=dict(nticks=5),
        xaxis_showspikes=False,
        yaxis_showspikes=False,
        zaxis_showspikes=False,
        aspectratio=dict(x=2, y=1, z=1)
    ),
    width=1920,
    height=1080,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Export to HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_HIST_YZ on x_VX_UNVX.html")

# Show plot
fig.show()