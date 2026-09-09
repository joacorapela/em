import math

# problem variables
epsilon0s = 8.85  # scale factor 1e12
alpha = math.pi / 6
d = 0.3
q1s = 1.0  # scale factor 1e6
q2s = 2.0  # scale factor 1e6
q3s = 0.5  # scale factor 1e6

# F1
absF21 = 1.0 / (4 * math.pi * epsilon0s) * q1s * q2s / d**2
d2 = 2 * d * math.sin((math.pi - alpha) / 2)
absF31 = 1.0 / (4 * math.pi * epsilon0s) * q1s * q3s / d2**2
F1 = (-(absF21 - absF31 * math.cos(alpha / 2)), absF31 * math.sin(alpha / 2))

print(f"F1={F1}")

# F2
absF32 = 1.0 / (4 * math.pi * epsilon0s) * q2s * q3s / d**2
F2 = (-absF32 * math.cos(alpha) + absF21, -absF32 * math.sin(alpha))

print(f"F2={F2}")

# F3
F3 = (absF32 * math.cos(alpha) - absF31 * math.cos(alpha / 2),
      absF32 * math.sin(alpha) - absF31 * math.sin(alpha / 2))

print(f"F3={F3}")
