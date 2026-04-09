import numpy as np
import matplotlib.pyplot as plt

# ================================
# Inverted Pendulum (Simplified)
# ================================

dt = 0.01
T = 10
t = np.arange(0, T, dt)

# States
theta = np.zeros_like(t)   # angle (rad)
omega = np.zeros_like(t)   # angular velocity

# Initial condition (unstable)
theta[0] = 0.3  # radians (perturbation)
omega[0] = 0.0

# ================================
# Simplified "HSB-like" Controller
# ================================

Kp = 5.0
Kd = 1.5

for i in range(len(t) - 1):
    # Control (placeholder)
    u = -Kp * theta[i] - Kd * omega[i]

    # Pendulum dynamics (simplified linearized)
    omega[i+1] = omega[i] + dt * (u + np.sin(theta[i]))
    theta[i+1] = theta[i] + dt * omega[i]

# ================================
# Plot (IEEE-style clean)
# ================================

plt.figure()
plt.plot(t, theta, label="Angle θ (rad)")
plt.plot(t, omega, label="Angular velocity ω")
plt.xlabel("Time [s]")
plt.ylabel("States")
plt.title("Inverted Pendulum Stabilization (Demo)")
plt.legend()
plt.grid()

# Save for README / paper
plt.savefig("../results/figures/pendulum_stabilization.png", dpi=300)

plt.show()

# ================================
# Output
# ================================

print("Final theta:", theta[-1])
print("Final omega:", omega[-1])
