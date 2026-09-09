import numpy as np
import plotly.figure_factory as ff


def E(p, q, d, epsilon0s=8.85*1e-6):
    # q should be given in micro Coulomb
    # answer return in Newton / Coulomb

    p_plus = -d/2 + 0j
    p_minus = d/2 + 0j
    E_plus = (1 / (4 * np.pi * epsilon0s) *
              q * (p - p_plus) / np.abs(p - p_plus)**3)
    E_minus = (-1 / (4 * np.pi * epsilon0s) *
               q * (p - p_minus) / np.abs(p - p_minus)**3)
    E = E_plus + E_minus

    return E


# define constants
q = 0.1  # micro Coulomb
d = 8.0  # meter
dx = 0.8
epsilon_x = 0.95
y_min = -10.0
y_max = 10.0
dy = 0.5
xlim = (-d, d)
factor_x = 3
fig_filename_pattern = "../../figures/6c.{:s}"

# Quiver parameters
quiver_scale = 0.0007
quiver_arrow_scale = 0.3
quiver_arrow_angle = np.pi / 4
quiver_width = 3

# calculate
xs1 = np.arange(factor_x * -d/2, -d/2 - epsilon_x, dx)
xs2 = np.arange(-d/2 + epsilon_x, d/2 - epsilon_x, dx)
xs3 = np.arange(d/2 + epsilon_x, d/2 * factor_x, dx)
xs = np.concatenate([xs1, xs2, xs3])

ys = np.arange(y_min, y_max, dy)

Xs, Ys = np.meshgrid(xs, ys)

p = Xs + 1j * Ys

e = E(p=p, q=q, d=d)

# plot
fig = ff.create_quiver(
    x=Xs,
    y=Ys,
    u=e.real,
    v=e.imag,
    scale=quiver_scale,
    arrow_scale=quiver_arrow_scale,
    angle=quiver_arrow_angle,
    scaleratio=1,
)
fig.add_vline(x=-d/2)
fig.add_vline(x=d/2)
fig.update_xaxes(title="x")
fig.update_yaxes(title="y", scaleanchor="x", scaleratio=1)
fig.update_traces(line=dict(width=quiver_width))
fig.update_layout(showlegend=False)
fig.write_html(fig_filename_pattern.format("html"))
fig.write_image(fig_filename_pattern.format("png"))
print("Saved " + fig_filename_pattern.format("html"))
