import math


def E(z0, sigmas, epsilon0s, R):
    answer = (0,
              0,
              (z0 * sigmas / (2 * epsilon0s) *
               (1.0 / abs(z0) - 1.0 / math.sqrt(R**2 + z0**2))))
    return answer


# problem variables
epsilon0s = 8.85  # scale factor 1e12
z0 = 0.1
R = 0.05
sigmas = 0.5  # scale factor 1e6

answer = E(z0=z0, sigmas=sigmas, epsilon0s=epsilon0s, R=R)
print(rf"answer=({answer[0]:.4f},{answer[1]:.4f},{answer[2]:.4f}) N/\mu C")
