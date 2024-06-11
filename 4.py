import math

# Given data
force_constant = 2400 
mass = 6.0
displacement = 0.04
compression_displacement = 0.02

# (a) Frequency of oscillation
frequency = (1 / (2 * math.pi)) * math.sqrt(force_constant / mass)
print("Frequency of oscillation:", frequency, "Hz")

# (b) Maximum acceleration of the mass
# Maximum acceleration occurs at maximum displacement
max_acceleration = (force_constant / mass) * displacement
print("Maximum acceleration of the mass:", max_acceleration, "m/s^2")

# (c) Maximum speed of the mass
# Maximum speed occurs at equilibrium position
max_speed = displacement * math.sqrt(force_constant / mass)
print("Maximum speed of the mass:", max_speed, "m/s")

# (d) Speed of the mass when the spring is compressed by 2.0 cm
# Using conservation of energy
speed_compressed = math.sqrt((force_constant / mass) * (displacement**2 - compression_displacement**2))
print("Speed of the mass when compressed by 2.0 cm:", speed_compressed, "m/s")

# (e) Potential energy of the mass when it momentarily comes to rest
# Potential energy at maximum displacement
potential_energy_rest = 0.5 * force_constant * displacement**2
print("Potential energy when it momentarily comes to rest:", potential_energy_rest, "J")

# (f) Total energy of the oscillating mass
# Total energy is constant and is the same as the potential energy at maximum displacement
total_energy = potential_energy_rest
print("Total energy of the oscillating mass:", total_energy, "J")
