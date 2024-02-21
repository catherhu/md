import numpy as np
import md


argon_atom = md.particle(40, np.array([0,0,0]), np.array([1,0,0]))
my_system = md.system(1)
my_system.add_particle(argon_atom)

#testing
for particle in my_system.particles:
    print(particle.m)
    print(particle.r)
    print(particle.v)

t = 1
dt = 0.001

my_system.verlet_evolve(dt)

#testing
for particle in my_system.particles:
    print(particle.m)
    print(particle.r)
    print(particle.v)