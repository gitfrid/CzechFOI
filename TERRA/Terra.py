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
# Create a 3D surface plot with a color bar
fig = go.Figure(data=[go.Surface(
    x=xi, y=yi, z=zi, 
    colorscale='HSV',
    colorbar=dict(title='Number of Deaths')  # Add a color bar with a title
)])



# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='Day of Death from 2020-01-01',
        yaxis_title='Age of Death',
        zaxis_title='Number of Deaths',
        xaxis=dict(nticks=20),  # Increase the number of ticks on the x-axis
        yaxis=dict(nticks=6),
        zaxis=dict(nticks=5),
        xaxis_showspikes=False,
        yaxis_showspikes=False,
        zaxis_showspikes=False,
        aspectratio=dict(x=2, y=1, z=1)  # Adjust aspect ratio to stretch x-axis
    ),
    width=1920,
    height=1080,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Export to HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_VX_UNVX.html")
#fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_VX.html")
#fig.write_html(r"C:\github\CzechFOI\3D Plot Results\TERRA_UNVX.html")


# Show plot
fig.show()