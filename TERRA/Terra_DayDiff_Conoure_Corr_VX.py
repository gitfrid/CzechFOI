import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from scipy.stats import pearsonr

# Load the data
data = pd.read_csv(r"C:\github\CzechFOI\TERRA\Terra_DayDiff_VX.csv")
# Calculate the difference
data['Difference'] = data['DAYSD_20200101'] - data['DAYSVD1_20200101']

# Calculate correlations
corr_age_diff, _ = pearsonr(data['AGE_D'], data['Difference'])
corr_age_daysd, _ = pearsonr(data['AGE_D'], data['DAYSD_20200101'])
corr_diff_daysd, _ = pearsonr(data['Difference'], data['DAYSD_20200101'])

# Create a grid for the surface plot
x = np.linspace(data['DAYSD_20200101'].min(), data['DAYSD_20200101'].max(), 100)
y = np.linspace(data['AGE_D'].min(), data['AGE_D'].max(), 100)
x_grid, y_grid = np.meshgrid(x, y)

# Interpolate the z values (Difference) on the grid using griddata
z_grid = griddata((data['DAYSD_20200101'], data['AGE_D']), data['Difference'], (x_grid, y_grid), method='cubic')

# Create the 3D surface plot with contours
fig = go.Figure(data=[go.Surface(
    x=x_grid,
    y=y_grid,
    z=z_grid,
    colorscale='Viridis',
    contours={
        "x": {"show": True, "start": x.min(), "end": x.max(), "size": 5},
        "y": {"show": True, "start": y.min(), "end": y.max(), "size": 5},
        "z": {"show": True, "start": z_grid.min(), "end": z_grid.max(), "size": 5}
    }
)])

# Add correlation annotations
fig.add_trace(go.Scatter3d(
    x=[data['DAYSD_20200101'].max()],
    y=[data['AGE_D'].max()],
    z=[data['Difference'].max()],
    mode='text',
    text=[f'Corr(AGE_D, Difference): {corr_age_diff:.2f}<br>Corr(AGE_D, DAYSD_20200101): {corr_age_daysd:.2f}<br>Corr(Difference, DAYSD_20200101): {corr_diff_daysd:.2f}'],
    showlegend=False
))

# Update layout for better visualization
fig.update_layout(scene=dict(
    xaxis_title='DAYSD_20200101',
    yaxis_title='AGE_D',
    zaxis_title='DAYSD_20200101 - DAYSVD1_20200101'
))

fig.write_html(r"C:\github\CzechFOI\3D Plot Results\Terra_DayDiff_Contoure_Corr_VX.html")

# Show the plot
fig.show()