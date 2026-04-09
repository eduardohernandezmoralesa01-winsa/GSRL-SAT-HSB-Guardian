import numpy as np
import matplotlib.pyplot as plt

# ================================
# Simplified Satellite Model (Demo)
# ================================

dt = 0.01
T = 10
t = np.arange(0, T, dt)

# States
theta = np.zeros_like(t)   # angle
omega = np.zeros_like(t)   # angular velocity

# Initial condition (disturbance)
theta[0] = 0.2   # radians
omega[0] = 0.0

# ================================
# Simplified "HSB-like" Controller
# (Non-proprietary placeholder)
# ================================

Kp = 2.0
Kd = 0.5

for i in range(len(t) - 1):
    # Control law (demo only, NOT real HSB)
    u = -Kp * theta[i] - Kd * omega[i]

    # Simple rotational dynamics (unit inertia)
    omega[i+1] = omega[i] + dt * u
    theta[i+1] = theta[i] + dt * omega[i]

# ================================
# Plot Results
# ================================

plt.figure()
plt.plot(t, theta, label="Angle (theta)")
plt.plot(t, omega, label="Angular velocity (omega)")
plt.xlabel("Time [s]")
plt.ylabel("State")
plt.title("Satellite Attitude Stabilization (Demo)")
plt.legend()
plt.grid()

# Save figure for README / IEEE
plt.savefig("../results/figures/satellite_stabilization.png")

plt.show()

# ================================
# Console Output
# ================================

print("Final angle (theta):", theta[-1])
print("Final angular velocity (omega):", omega[-1])
