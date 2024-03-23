import md


n = 100 # number of particles
m = 1 # mass, reduced units
t = 1e-7 # total time
dt = 1e-10 # time step
T = 2.5 # initial temperature, reduced units
system_size = 1 # reduced units

my_system = md.system() 

my_system.add_particles(m, n, T, system_size)

my_system.verlet_simulate(dt, t, n)


