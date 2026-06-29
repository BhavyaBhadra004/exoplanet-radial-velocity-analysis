"""
Keplerian radial velocity model.

Author: Bhavya Ajay
"""

import numpy as np
import matplotlib.pyplot as plt

def keplerian_model(t, K, P, phi, V):
    return K * np.sin(2 * np.pi * t / P + phi) + V

K = 461       # m/s
P = 3.312     # days
phi = 0       # start at 0
V = 0         # systemic velocity

time = np.linspace(0, 20, 500)   # time from 0 to 20 days
radial_velocity = keplerian_model(time, K, P, phi, V)

plt.figure(figsize=(10, 5))
plt.plot(time, radial_velocity)
plt.xlabel("Time (days)")
plt.ylabel("Radial Velocity (m/s)")
plt.title("Radial Velocity Curve for Tau Boo b")
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlim(0, 20)   # explicitly ensure x-axis starts at 0
plt.show()
