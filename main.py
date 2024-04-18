import md


unit_cell_size = 1.7 # for liquid argon, density = 1.374 g/L
lattice_dim = 4 # corresponds to 108 particles
t = 5 # total time
dt = 0.01 # time step
m = 1 # mass
T = 0.75 # initial temperature


my_system = md.system() 

my_system.add_particles(unit_cell_size, lattice_dim, m, T)

my_system.verlet_simulate(dt, t)


