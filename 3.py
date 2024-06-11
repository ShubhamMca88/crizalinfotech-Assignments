import math

# Given data
mass = 2  # kg
displacement = 0.1  # m

# Calculate force constant
force_constant = (mass * 9.8) / displacement  # F = mg
print("Force constant of the spring:", force_constant, "N/m")

# Calculate period of oscillations when the body is pulled down slightly and released
period = 2 * math.pi * math.sqrt(mass / force_constant)
print("Period of oscillations when released:", period, "seconds")

# Calculate period of SHM on a frictionless horizontal surface
period_horizontal = period
print("Period of SHM on a frictionless horizontal surface:", period_horizontal, "seconds")
