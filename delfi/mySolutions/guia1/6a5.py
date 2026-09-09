import numpy as np
import plotly.graph_objects as go


def E_x(x, q, d, epsilon0s=8.85*1e-6):
    # q should be given in micro Coulomb
    # answer return in Newton / Coulomb
    answer = (q / (4 * np.pi * epsilon0s) *
              (1.0 / (x + d / 2)**2 - 1.0 / (x - d / 2)**2))
    return answer


# define constants
q = 0.1  # micro Coulomb
d = 8.0  # 1 meter
dx = 0.01
epsilon_x = 0.8
factor_x = 3
fig_filename_pattern = "../../figures/6a5.{:s}"

xs1 = np.arange(factor_x * -d/2, -d/2 - epsilon_x, dx)
xs2 = np.arange(-d/2 + epsilon_x, d/2 - epsilon_x, dx)
xs3 = np.arange(d/2 + epsilon_x, d/2 * factor_x, dx)

# calculate
absE_xs1 = np.abs(E_x(x=xs1, q=q, d=d))
absE_xs2 = np.abs(E_x(x=xs2, q=q, d=d))
absE_xs3 = np.abs(E_x(x=xs3, q=q, d=d))

# plot
fig = go.Figure()
trace = go.Scatter(x=xs1, y=absE_xs1, mode="lines+markers",
                   line=dict(color="blue"))
fig.add_trace(trace)
trace = go.Scatter(x=xs2, y=absE_xs2, mode="lines+markers",
                   line=dict(color="blue"))
fig.add_trace(trace)
trace = go.Scatter(x=xs3, y=absE_xs3, mode="lines+markers",
                   line=dict(color="blue"))
fig.add_trace(trace)
fig.add_vline(x=-d/2)
fig.add_vline(x=d/2)
fig.update_xaxes(title="x")
fig.update_yaxes(title="|E(x, 0)| (N/C)")
fig.update_layout(showlegend=False)
fig.write_html(fig_filename_pattern.format("html"))
fig.write_image(fig_filename_pattern.format("png"))
print("Saved " + fig_filename_pattern.format("html"))
