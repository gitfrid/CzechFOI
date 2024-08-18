import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import griddata

# Load data
chunk = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_VX_UNVX.csv", comments='#', delimiter=',', skiprows=1)
#chunk  = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_VX.csv",comments='#',delimiter=',',skiprows=1)
#chunk  = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_UNVX.csv",comments='#',delimiter=',',skiprows=1)
DATA = np.array(chunk)
Ys = DATA[:, 0]
Xs = DATA[:, 1]
Zs = DATA[:, 2]

# Create a grid for the surface plot
xi = np.linspace(Xs.min(), Xs.max(), 100)
yi = np.linspace(Ys.min(), Ys.max(), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((Xs, Ys), Zs, (xi, yi), method='linear')

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(x=xi, y=yi, z=zi, colorscale='HSV')])

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='Day of Death from 2020-01-01',
        yaxis_title='Age of Death',
        zaxis_title='Number of Deaths',
        xaxis=dict(nticks=5),
        yaxis=dict(nticks=6),
        zaxis=dict(nticks=5),
        xaxis_showspikes=False,
        yaxis_showspikes=False,
        zaxis_showspikes=False
    ),
    width=1920,
    height=1080,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Export to HTML
#fig.write_html("path/to/your_plot.html")

# Show plot
fig.show()