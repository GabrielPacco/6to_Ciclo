import plotly.graph_objects as go
import numpy as np

N = 30     # Number of boxes

# generar una matriz de colores del arco iris mediante la fijación de la saturación y la luminosidad de la HSL
# representación del color y marchando alrededor del tono.
# Plotly acepta cualquier formato de color CSS, véase, por ejemplo, http://www.w3schools.com/cssref/css_colors_legal.asp.
c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

# Cada caja está representada por un dict que contiene los datos, el tipo y el color.
# Usa la comprensión de la lista para describir N cajas, cada una con un color diferente y con diferentes datos generados aleatoriamente:
fig = go.Figure(data=[go.Box(
    y=3.5 * np.sin(np.pi * i/N) + i/N + (1.5 + 0.5 * np.cos(np.pi*i/N)) * np.random.rand(10),
    marker_color=c[i]
    ) for i in range(int(N))])

# format the layout
fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(zeroline=False, gridcolor='white'),
    paper_bgcolor='rgb(233,233,233)',
    plot_bgcolor='rgb(233,233,233)',
)

fig.show()