import numpy as np
import pandas as pd
import plotly.express as px

data = {
    'x': [],
    'y': [],
    'z': [],
    'size': [],
    'color': [],
    }

side = 3

for x in range(1, side+1):
    for y in range(1, side+1):
        for z in range(1, side+1):
            size = (x * y * z / side**3) * 100
            color = np.log10((side**3)/(x * y * z))
            data['x'].append(x)
            data['y'].append(y)
            data['z'].append(z)
            data['size'].append(size)
            data['color'].append(color)

df = pd.DataFrame(data)

fig = px.scatter_3d(df,
                    x='x',
                    y='y',
                    z='z',
                    color='color',
                    size='size',
                    size_max=df['size'].max(),
                    title='plotly',
                    opacity=0.8,
                    color_continuous_scale='viridis',
                    )

fig.update_layout(margin=dict(l=0, r=0, b=0, t=50))

fig.write_html('filename.html')

fig.show()