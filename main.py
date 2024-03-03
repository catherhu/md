import numpy as np
import md


n = 100
m = 1 # mass
t = 1E-7 # total time
dt = 1E-10 # time step
T = 1 # initial temperature


my_system = md.system()

my_system.add_particles(m, n, T)

my_system.verlet_simulate(dt, t, n)



