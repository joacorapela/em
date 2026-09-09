import numpy as np
import plotly.figure_factory as ff


def E_y(y, q, d, epsilon0s=8.85*1e-6):
    # q should be given in micro Coulomb
    # answer return in Newton / Coulomb

    E_y = q * d / ((4 * np.pi * epsilon0s) * ((d / 2)**2 + y**2)**1.5)
    return E_y


# define constants
q = 0.1  # micro Coulomb
d = 8.0  # meter
y_min = -30.0
y_max = 30.0
dy = 0.5
xlim = (-1.0, 1.0)
fig_filename_pattern = "../../figures/6b.{:s}"

# Quiver parameters
quiver_scale = 0.007
quiver_arrow_scale = 0.3
quiver_arrow_angle = np.pi / 3
quiver_width = 3

ys = np.arange(y_min, y_max, dy)

# calculate
E_ys = E_y(y=ys, q=q, d=d)

# plot
fig = ff.create_quiver(
    x=np.zeros_like(ys),
    y=ys,
    u=E_ys,
    v=np.zeros_like(E_ys),
    scale=quiver_scale,
    arrow_scale=quiver_arrow_scale,
    angle=quiver_arrow_angle,
)
fig.add_vline(x=-d/2)
fig.add_vline(x=d/2)
fig.update_yaxes(title="y", scaleanchor="x", scaleratio=1)
fig.update_xaxes(title="x", range=xlim)
fig.update_traces(line=dict(width=quiver_width))
fig.update_layout(showlegend=False)
fig.write_html(fig_filename_pattern.format("html"))
fig.write_image(fig_filename_pattern.format("png"))
print("Saved " + fig_filename_pattern.format("html"))
