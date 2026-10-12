import math


def sign(x):
    return (x > 0) - (x < 0)


lambdas = 20.0  # 10^{-6}
Qs = 8.0  # 10^{-6}
epsilon0s = 8.85  # 10^{-12}
x = 0.2  # meter
d = 0.4
b = 0.6
c = -0.6
q2s = -2.0

E_H = (lambdas / (4*math.pi*epsilon0s) * 10 / math.sqrt(5))
E_Q = (1.0 / (4*math.pi*epsilon0s) *
       Qs / (x - d)**2 * sign(x - d))  # N / \mu C
E = E_H + E_Q

print("Parte a")
print(f"E_H={E_H}")
print(f"E_Q={E_Q}")
print(f"E={E}")

x_Q = 0.2 + math.sqrt(1.0 / (4*math.pi*epsilon0s) * Qs / E_H)  # N / \mu C

print("Parte b")
print(f"x_Q={x_Q}")

W = (1.0 / (4*math.pi*epsilon0s) * q2s * Qs * 
     (1.0 / abs(d - c) - 1.0 / abs(d - b)))  # N * m
print("Parte c")
print(f"W={W}")

