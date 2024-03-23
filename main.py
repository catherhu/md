import md


n = 10
m = 1 # mass
t = 1E-9 # total time
dt = 1E-10 # time step
T = 1 # initial temperature
box_size = 1

my_system = md.system()

my_system.add_particles(m, n, T, box_size)

my_system.verlet_simulate(dt, t, n)


