import md

unit_cell_size = 15 # for argon gas
#unit_cell_size = 1.7 # for liquid argon
lattice_dim = 3 # number of units cells along an axis (number of particles = 4 * lattice_dim ^ 3)
t = 3 # total time
dt = 0.01 # time step
m = 1 # mass
#T = 0.8 # initial temperature
T = 2.5 # initial temperature
separation = 1.2

my_system = md.system() 

#my_system.two_particles(m, separation)

my_system.add_particles_lattice(unit_cell_size, lattice_dim, m, T)

#my_system.verlet_simulate(dt, t)

my_system.verlet_simulate(dt, t, unit_cell_size, lattice_dim, T)

#my_system.verlet_simulate(dt, t, unit_cell_size, lattice_dim, T, boundaries = True, thermostat = True)
