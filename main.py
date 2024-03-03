import numpy as np
import md


"""
p = 15E6 # initial pressure in Pa
R = 8.314 # ideal gas constant
N_a = 6.022E23 # avogadro constant
a = 3.59
b = 3.34E-5
"""

n = 10
V = 1E-6 # volume in cubic meters
m_a = 40 # argon atomic mass
t = 1 # total time
dt = 0.001 # time step
T = 298 # initial temperature

m = m_a * 1.66E-27

my_system = md.system()

my_system.add_particles(m, n, T, V)

# testing
for p in my_system.particles:
    print(p.r)
    print(p.v)

my_system.verlet_simulate(dt, t, n)

# testing
for p in my_system.particles:
    print(p.r)
    print(p.v)
