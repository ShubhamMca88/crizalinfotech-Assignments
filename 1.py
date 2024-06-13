""" Question 1 :  The time-period of a simple pendulum is 4 s and it can go to and fro from equilibriu position at a maximum distance of 10 cm. 
                If at the start of the motion the pendulum is in the position nt maximum displacement towards the right of the equilibrium 
                position, then write the displacement eguation of the pendulum. """
                
# .........................................................solution by shubham.......................................................

import sympy as sp

t = sp.symbols('t')

# Given values
A = 0.1
T = 4

# Calculate the angular frequency
omega = 2 * sp.pi / T

# Phase constant φ is 0 because it starts at maximum displacement
phi = 0

# Displacement equation x(t) = A * cos(omega * t + phi)
x_t = A * sp.cos(omega * t + phi)

# Display the displacement equation
print(f"The displacement equation of the pendulum is: x(t) = {x_t}")
