# Question 2 : A block is resting on a piston which is moving vertically in simple harmonic motion of period 2.0 s. At what amplitude of motion will the
# block and piston separate? What is the maximum velocity of the piston at this amplitude?

# .........................................................solution by shubham.......................................................

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
