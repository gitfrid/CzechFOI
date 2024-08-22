import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import griddata

# Load data
chunk = np.loadtxt(r"C:\github\CzechFOI\TERRA\TERRA_UNVX.csv", comments='#', delimiter=',', skiprows=1)
DATA = np.array(chunk)
Ys = DATA[:, 0]
Xs = DATA[:, 1]
Zs = DATA[:, 2]

# Create a grid for the surface plot
xi = np.linspace(Xs.min(), Xs.max(), 100)
yi = np.linspace(Ys.min(), Ys.max(), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((Xs, Ys), Zs, (xi, yi), method='linear')

# Replace NaN values in zi
zi = np.nan_to_num(zi, nan=np.nanmin(zi))

# Debugging print statements
print("xi:", xi)
print("yi:", yi)
print("zi:", zi)

# Create a 3D surface plot with contour lines
fig = go.Figure(data=[go.Surface(
    x=xi, y=yi, z=zi, 
    colorscale='HSV',  # Changed to HSV colormap
    contours=dict(
        x=dict(show=True, start=xi.min(), end=xi.max(), size=(xi.max() - xi.min()) / 10),
        y=dict(show=True, start=yi.min(), end=yi.max(), size=(yi.max() - yi.min()) / 10),
        z=dict(show=True, start=zi.min(), end=zi.max(), size=(zi.max() - zi.min()) / 10)
    ),
    colorbar=dict(title='Number of Deaths')
)])

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='Day of Death from 2020-01-01',
        yaxis_title='Age of Death',
        zaxis_title='Number of Deaths',
        aspectratio=dict(x=2, y=1, z=0.5)
    ),
    width=1920,
    height=1080,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Export to HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_3DContour_UNVX.html")

# Show plot
fig.show()