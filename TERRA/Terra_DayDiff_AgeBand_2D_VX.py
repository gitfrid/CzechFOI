import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load the data
data = pd.read_csv(r"C:\github\CzechFOI\TERRA\Terra_DayDiff_VX.csv")

# Calculate the difference
data['Difference'] = data['DAYSD_20200101'] - data['DAYSVD1_20200101']

# Define age bands
data['Age_Band'] = pd.cut(data['AGE_D'], bins=np.arange(0, data['AGE_D'].max() + 5, 5), right=False)

# Create a color palette
color_palette = px.colors.qualitative.Plotly

# Create subplots
fig = make_subplots(rows=len(data['Age_Band'].unique()), cols=1, shared_xaxes=False, 
                    subplot_titles=[f'Age Band {age_band}' for age_band in data['Age_Band'].unique()])

# Add traces for each age band
for i, age_band in enumerate(data['Age_Band'].unique()):
    age_band_data = data[data['Age_Band'] == age_band]
    fig.add_trace(go.Scatter(x=age_band_data['DAYSD_20200101'], y=age_band_data['Difference'], 
                             mode='lines+markers', name=f'Age Band {age_band}', 
                             line=dict(color=color_palette[i % len(color_palette)])), 
                  row=i+1, col=1)

# Update layout to show x-axis labels for each subplot
fig.update_layout(height=800*len(data['Age_Band'].unique()), title_text='DAYSD_20200101 vs Difference by Age Bands', 
                  showlegend=False)

# Ensure x-axis labels are shown for each subplot
for i in range(1, len(data['Age_Band'].unique()) + 1):
    fig.update_xaxes(showticklabels=True, row=i, col=1)

# Save to HTML
fig.write_html(r"C:\github\CzechFOI\3D Plot Results\Terra_DayDiff_AgeBands_VX.html")

# Show the plot
fig.show()