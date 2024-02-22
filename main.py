import numpy as np
import md

n = 2 # number of particles
m = 40 # argon mass
t = 1 # total time
dt = 0.001 # time step

my_system = md.system()

my_system.add_particles(m, n)

# testing
for p in my_system.particles:
    print(p.m)
    print(p.r)
    print(p.v)

# evolve one step
my_system.verlet_simulate(dt, t, n)

# testing
for p in my_system.particles:
    print(p.m)
    print(p.r)
    print(p.v)
