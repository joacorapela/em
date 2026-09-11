import math
import plotly.graph_objects as go


def E(x0, y0, epsilon0s, L, aLambda):
    k = aLambda / (4 * math.pi * epsilon0s)
    answer = (k * (1.0 / math.sqrt((x0 - L/2)**2 + y0**2) -
                1.0 / math.sqrt((x0 + L/2)**2 + y0**2)),
               k * ((L/2 - x0) / (y0 * math.sqrt((L/2 - x0)**2 + y0**2)) +
                    (L/2 + x0) / (y0 * math.sqrt((L/2 + x0)**2 + y0**2))))
    return answer

def E_L_inf(y0, epsilon0s, aLambda):
    k = aLambda / (4 * math.pi * epsilon0s)
    answer = (0, k / (2 * y0))
    return answer

# problem variables
L = .5  # 50cm
aLambda = 15  # micro Coulomb / meter
epsilon0s = 8.85  # scale factor 1e12
x0 = 0.0
fig_filename_pattern = "../../figures/7bc.{:s}"
perc_fig_filename_pattern = "../../figures/7d.{:s}"

# calculate
y_start = 0.05
y_stop = 2.1
y_step = 0.01

num_steps = math.ceil((y_stop - y_start) / y_step)
y0s = [y_start + i * y_step for i in range(num_steps)]

norm_Es = [math.nan for i in range(num_steps)]
norm_E_L_infs = [math.nan for i in range(num_steps)]
perc_diff = [math.nan for i in range(num_steps)]
for i in range(len(y0s)):
    norm_Es[i] = E(x0=x0, y0=y0s[i],
                   epsilon0s=epsilon0s,
                   L=L, aLambda=aLambda)[1]  # N / micro Coulomb
    norm_E_L_infs[i] = E_L_inf(y0=y0s[i],
                               epsilon0s=epsilon0s,
                               aLambda=aLambda)[1]  # N / micro Coulomb
    perc_diff[i] = (norm_Es[i] - norm_E_L_infs[i]) / norm_E_L_infs[i]

# plot b and c
fig = go.Figure()
trace = go.Bar(x=y0s, y=norm_Es, name=f"L={L}m")
fig.add_trace(trace)
trace = go.Bar(x=y0s, y=norm_E_L_infs, name=r"$\text{L}=\infty$")
fig.add_trace(trace)
fig.update_xaxes(title=r"$y_0$")
fig.update_yaxes(
    title_text=r"$\| \mathbf{E}(0,y_0,0) \|_2 \quad [\text{N}/\mu\text{C}]$"
)
fig.write_html(fig_filename_pattern.format("html"), include_mathjax="cdn")
fig.write_image(fig_filename_pattern.format("png"))
print("Saved {:s}".format(fig_filename_pattern.format("html")))

# plot d
fig = go.Figure()
trace = go.Bar(x=y0s, y=perc_diff)
fig.add_trace(trace)
fig.update_xaxes(title=r"$y_0$")
fig.update_yaxes(title=r"$\frac{E_{L=0.5m}(0,y_0,0)-E_{L=\infty}(0,y_0,0)}{E_{L=\infty}(0,y_0,0)}$")
fig.write_html(perc_fig_filename_pattern.format("html"), include_mathjax="cdn")
fig.write_image(perc_fig_filename_pattern.format("png"))
print("Saved {:s}".format(perc_fig_filename_pattern.format("html")))

breakpoint()
