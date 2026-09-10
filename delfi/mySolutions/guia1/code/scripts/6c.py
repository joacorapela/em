import numpy as np
import plotly.graph_objects as go


def E(p, q, d, epsilon0s=8.85*1e-6):
    # p \in 3 \times N
    # q should be given in micro Coulomb
    # answer return in Newton / Coulomb
    # answer \in N \times 3
    p_plus = np.array([-d/2, 0.0, 0.0])
    p_minus = np.array([d/2, 0.0, 0.0])
    E_plus = (1 / (4 * np.pi * epsilon0s) * q * (p - p_plus) /
              (np.linalg.norm(p - p_plus, axis=1)**3)[:, np.newaxis])
    E_minus = (-1 / (4 * np.pi * epsilon0s) * q * (p - p_minus) /
               (np.linalg.norm(p - p_minus, axis=1)**3)[:, np.newaxis])
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
z_min = -2.0
z_max = 2.1
dz = 1.0
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
zs = np.arange(z_min, z_max, dz)

X, Y, Z = np.meshgrid(xs, ys, zs, indexing="ij")
p = np.stack([X, Y, Z], axis=-1).reshape(-1, 3)

e = E(p=p, q=q, d=d)
e_magnitudes = np.sqrt(np.sum(e**2, axis=1))
e_norm = e / e_magnitudes[:, np.newaxis]

# plot
fig = go.Figure()
trace = go.Cone(
    x=p[:, 0],
    y=p[:, 1],
    z=p[:, 2],
    u=e[:, 0],
    v=e[:, 1],
    w=e[:, 2],
    sizemode="scaled",
    sizeref=0.3,
    anchor="cm",
    colorbar=dict(title="Field Magnitude"),
    customdata=e_magnitudes,
    hovertemplate="<b>x:</b> %{x:.2f}<br>" +
                  "<b>y:</b> %{y:.2f}<br>" +
                  "<b>z:</b> %{z:.2f}<br>" +
                  "<b>Magnitude:</b> %{customdata:.2e}",
)
fig.add_trace(trace)

fig.update_layout(
    scene=dict(
        aspectmode="data",  # Preserves true 1:1 coordinate scale
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
    )
)

v_min = np.percentile(e_magnitudes, 5)
v_max = np.percentile(e_magnitudes, 95)

fig.update_traces(
    cmin=v_min,
    cmax=v_max
)
fig.write_html(fig_filename_pattern.format("html"))
fig.write_image(fig_filename_pattern.format("png"))
print("Saved " + fig_filename_pattern.format("html"))
