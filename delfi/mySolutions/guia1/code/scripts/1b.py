import math

q2s = 4.0  # scale factor 1e6
q1s = 1.5  # scale factor 1e6
d = ((-0.2 * q1s + math.sqrt((.2 * q1s)**2 + 4 * (q2s - q1s) * 0.1**2 * q1s)) /
     (2 * (q2s - q1s)))

print(f"d={d} m")

# absF = 5.3951
# epsilon0s = 8.85  # scale factor 1e12
# q0 = absF * d**2 / q2s * 4 * math.pi * epsilon0s  # micro Coulomb

# print(f"q0={q0} micro Coulomb")

q0 = (0.1 - d)**2 / 0.1**2 * q1s # micro Coulomb

print(f"q0={q0} micro Coulomb")

