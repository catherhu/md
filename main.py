import numpy as np
import md


"""
p = 15E6 # initial pressure in Pa
R = 8.314 # ideal gas constant
N_a = 6.022E23 # avogadro constant
a = 3.59
b = 3.34E-5
"""

n = 32
m = 1 # mass
t = 1E-12 # total time
dt = 1E-15 # time step
T = 1 # initial temperature


my_system = md.system()

my_system.add_particles(m, n, T)

my_system.verlet_simulate(dt, t, n)


# testing
for p in my_system.particles:
    print(p.r)
    print(p.v)