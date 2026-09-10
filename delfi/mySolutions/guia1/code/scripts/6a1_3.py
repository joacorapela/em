import numpy as np
import plotly.figure_factory as ff


def E_x(x, q, d, epsilon0s=8.85*1e-6):
    # q should be given in micro Coulomb
    # answer return in Newton / Coulomb

    answer = (q / (4 * np.pi * epsilon0s) *
              ((x + d / 2) / np.abs(x + d / 2)**3 -
               (x - d / 2) / np.abs(x - d / 2)**3))
    return answer


# define constants
q = 0.1  # micro Coulomb
d = 8.0  # 1 meter
dx = 0.8
epsilon_x = 0.95
ylim = [-1.0, 1.0]
factor_x = 3
fig_filename_pattern = "../../figures/6a1_3b.{:s}"

# Quiver parameters
quiver_scale = 0.0007
quiver_arrow_scale = 0.3
quiver_arrow_angle = np.pi / 8
quiver_width = 3

xs1 = np.arange(factor_x * -d/2, -d/2 - epsilon_x, dx)
xs2 = np.arange(-d/2 + epsilon_x, d/2 - epsilon_x, dx)
xs3 = np.arange(d/2 + epsilon_x, d/2 * factor_x, dx)
xs = np.concatenate([xs1, xs2, xs3])

# calculate
E_xs1 = E_x(x=xs1, q=q, d=d)
E_xs2 = E_x(x=xs2, q=q, d=d)
E_xs3 = E_x(x=xs3, q=q, d=d)
E_xs = np.concatenate([E_xs1, E_xs2, E_xs3])

# plot
fig = ff.create_quiver(
    x=xs,
    y=np.zeros_like(xs),
    u=E_xs,
    v=np.zeros_like(E_xs),
    scale=quiver_scale,
    arrow_scale=quiver_arrow_scale,
    angle=quiver_arrow_angle,
)
fig.add_vline(x=-d/2)
fig.add_vline(x=d/2)
fig.update_yaxes(title="y", scaleratio=1, range=ylim)
fig.update_xaxes(title="x")
fig.update_traces(line=dict(width=quiver_width))
fig.update_layout(showlegend=False)
fig.write_html(fig_filename_pattern.format("html"))
fig.write_image(fig_filename_pattern.format("png"))
print("Saved " + fig_filename_pattern.format("html"))
