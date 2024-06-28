import numpy as np
from itertools import product

class particle:
    def __init__ (self, position, velocity, mass, acceleration):
        self.r = position
        self.v = velocity
        self.m = mass
        self.a = acceleration
class system:
    def __init__ (self):
        self.particles = []

    def add_two_particles(self, m, separation):
        r = np.zeros(3)
        v = np.zeros(3)
        a = np.zeros(3)
        self.particles.append(particle(r, v, m, a))
        r = np.array([0, 0, separation])
        self.particles.append(particle(r, v, m, a))
    
    def add_particles_lattice(self, unit_cell_size, lattice_dim, m, T = 0):
        positions = np.array(list(product(range(lattice_dim), repeat=3))) * unit_cell_size
        offsets = np.array([[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0], [0, 0, 0]]) * unit_cell_size
        for p in positions:
            for o in offsets:
                r = p + o
                v = np.random.normal(0, np.sqrt(T), size=3)
                a = np.zeros(3)
                self.particles.append(particle(r, v, m, a))
    
    def calculate_temperature(self):
        kinetic_energy = 0.5 * np.sum([p.m * np.dot(p.v, p.v) for p in self.particles])
        T = 2 * kinetic_energy / (3 * len(self.particles))
        return T

    # calculating force between two particles:
    def lennard_jones(self, i, j):   
        r_i = self.particles[i].r
        r_j = self.particles[j].r
        s = np.linalg.norm(r_i - r_j)
        # particles far apart have negligible interactions
        if s > 3:
            return np.zeros(3)
        return 24 * (2 / s**12 - 1 / s**6) * (r_i - r_j) / s**2

    # calculating total force from all particles acting on a chosen particle:
    def total_force_particles(self, i): 
        F = np.zeros(3)
        n = len(self.particles)
        for j in range(n):
            if j != i:
                F += self.lennard_jones(i, j)
        return F

    # system evolution for a single step:
    def verlet_evolve(self, dt, unit_cell_size, lattice_dim, target_temp, boundaries, thermostat):
        n = len(self.particles)
        # calculate acceleration for all particles:
        for i in range(n):
            F = self.total_force_particles(i)
            self.particles[i].a = F/self.particles[i].m
        # write to file and update velocities and positions for all particles:
        for p in self.particles:
            p.v = p.v + 0.5*p.a*dt
            p.r = p.r + p.v*dt
        # again calculate acceleration for all particles:
        for i in range(n):       
            F = self.total_force_particles(i)
            self.particles[i].a = F/self.particles[i].m
        # update velocities for all particles:
        for p in self.particles:
            p.v = p.v + 0.5*p.a*dt
            if boundaries:
                # reflective boundaries:
                if any(p.r[k] > unit_cell_size * (lattice_dim - 0.5) or p.r[k] < 0 for k in range(3)):
                    p.v = -p.v
        if thermostat:
            # apply Berendsen thermostat
            current_temp = self.calculate_temperature()
            tau = 0.1
            lambda_factor = np.sqrt(1 + (dt / tau) * (target_temp / current_temp - 1))
            for p in self.particles:
                p.v *= lambda_factor

    # system evolution through time:     
    def verlet_simulate(self, dt, t, unit_cell_size = None, lattice_dim = None, target_temp = None, boundaries = False, thermostat = False):
        n_iter = int(t/dt)
        n = len(self.particles)
        with open('md.txt', 'w') as md_file, open('temp.txt', 'w') as temp_file:
            for i in range(n_iter):
                md_file.write(f"{n}\n")
                md_file.write("type                    x                    y                    z\n")
                for p in self.particles:
                    md_file.write(f"Ar          {p.r[0]:.10f}          {p.r[1]:.10f}          {p.r[2]:.10f}\n")
                self.verlet_evolve(dt, unit_cell_size, lattice_dim, target_temp, boundaries, thermostat)
                time = (i + 1) * dt
                T = self.calculate_temperature()
                temp_file.write(f"{time:.2f}\t{T}\n")
            # write last step to file:
            md_file.write(f"{n}\n")
            md_file.write("type                    x                    y                    z\n")
            for p in self.particles:
                md_file.write(f"Ar          {p.r[0]:.10f}          {p.r[1]:.10f}          {p.r[2]:.10f}\n")