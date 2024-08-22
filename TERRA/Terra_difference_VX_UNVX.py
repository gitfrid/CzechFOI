import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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

# Calculate differences
differences = np.diff(zi, axis=0)

# Create subplots
fig = make_subplots(rows=2, cols=1, subplot_titles=('Original Data', 'Differences Between Consecutive Points'))

# Original data plot
fig.add_trace(go.Heatmap(z=zi, colorscale='Viridis'), row=1, col=1)

# Differences plot
fig.add_trace(go.Heatmap(z=differences, colorscale='Viridis'), row=2, col=1)

# Update layout
fig.update_layout(height=800, width=800, title_text="Surface Plot and Differences")

# Save as HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_difference_UNVX.html")

# Show plot in browser
fig.show()