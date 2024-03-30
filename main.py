import md


n = 100 # number of particles
t = 1 # total time
dt = 1e-3 # time step
m = 1
T = 0.75 # initial temperature, reduced units
system_size = 1 # reduced units

my_system = md.system() 

my_system.add_particles(n, m, T, system_size)

my_system.verlet_simulate(dt, t, n)


