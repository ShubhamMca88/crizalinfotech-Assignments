import math

# Given data
T = 2.0  # period of motion in seconds

# Calculating angular frequency
omega = 2 * math.pi / T

# Maximum displacement (amplitude) occurs when sin(omega*t) = 1
A = 1

# Maximum velocity at amplitude A
v_max = A * omega

print("Amplitude of motion at which the block and piston separate:", A, "m")
print("Maximum velocity of the piston at this amplitude:", round(v_max, 2), "m/s")
