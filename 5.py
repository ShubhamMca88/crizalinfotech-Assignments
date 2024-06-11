import math

# Given data
initial_length = 1.0
initial_g = 9.8

# Initial period calculation
initial_period = 2 * math.pi * math.sqrt(initial_length / initial_g)

# (i) Length increased by 5%
new_length = initial_length * 1.05
new_period_length = 2 * math.pi * math.sqrt(new_length / initial_g)
percentage_change_length = ((new_period_length - initial_period) / initial_period) * 100

# (ii) Mass increased by 40% (no effect on period)
percentage_change_mass = 0

# (iii) Oscillation amplitude decreased by 10% (no effect on period for small angles)
percentage_change_amplitude = 0

# (iv) g increased by 0.16%
new_g = initial_g * 1.0016
new_period_g = 2 * math.pi * math.sqrt(initial_length / new_g)
percentage_change_g = ((new_period_g - initial_period) / initial_period) * 100

# Output results
print(f"Percentage change in the period if the length is increased by 5%: {percentage_change_length:.4f}%")
print(f"Percentage change in the period if the mass is increased by 40%: {percentage_change_mass:.4f}%")
print(f"Percentage change in the period if the oscillation amplitude is decreased by 10%: {percentage_change_amplitude:.4f}%")
print(f"Percentage change in the period if g is increased by 0.16%: {percentage_change_g:.4f}%")
