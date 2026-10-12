import math


def sign(x):
    return (x > 0) - (x < 0)


lambdas = 20.0  # 10^{-6}
Qs = 8.0  # 10^{-6}
epsilon0s = 8.85  # 10^{-12}
x = 0.2  # meter
D = 0.4
B = 0.6
C = -0.6
q2s = -2.0

E_H = (lambdas / (4*math.pi*epsilon0s) *
       0.2 / (x * math.sqrt(x**2 + 0.1**2)))  # N / \mu C
E_Q = (1.0 / (4*math.pi*epsilon0s) *
       Qs / (x - D)**2 * sign(x - D))  # N / \mu C
E = E_H + E_Q

print("Parte a")
print(f"E_H={E_H}")
print(f"E_Q={E_Q}")
print(f"E={E}")

x_Q = 0.2 + math.sqrt(1.0 / (4*math.pi*epsilon0s) * Qs / E_H)  # N / \mu C

print("Parte b")
print(f"x_Q={x_Q}")

W = (1.0 / (4*math.pi*epsilon0s) * q2s * Qs * 
     (1.0 / abs(D - C) - 1.0 / abs(D - B)))  # N * m
print("Parte c")
print(f"W={W}")

