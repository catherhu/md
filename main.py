import md

#unit_cell_size = 15 # for argon gas
unit_cell_size = 1.7 # for liquid argon, density = 1.374 g/L
lattice_dim = 3 # number of particles = 4 * 3^3 lattice_dim
t = 5 # total time
dt = 0.01 # time step
m = 1 # mass
#T =  # initial temperature


my_system = md.system() 

my_system.add_particles(unit_cell_size, lattice_dim, m, T)

my_system.verlet_simulate(dt, t, unit_cell_size, lattice_dim)


