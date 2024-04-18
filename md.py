import numpy as np
import matplotlib.pyplot as plt
from itertools import product
#from joblib import Parallel, delayed


class particle:
    def __init__ (self, position, velocity, mass):
        self.r = position
        self.v = velocity
        self.m = mass
class system:
    def __init__ (self):
        self.particles = []
    
    def add_particles(self, unit_cell_size, lattice_dim, m, T):
        for x in range(lattice_dim): 
            for y in range(lattice_dim):
                for z in range(lattice_dim):

                    r = np.array([x, y, z]) * unit_cell_size 
                    v = np.zeros(3)
                    #v = np.random.normal(0, np.sqrt(T), size = 3) 
                    self.particles.append(particle(r, v, m))

                    r = np.array([x, y + 0.5, z + 0.5]) * unit_cell_size 
                    v = np.zeros(3)
                    #v = np.random.normal(0, np.sqrt(T), size = 3) 
                    self.particles.append(particle(r, v, m))

                    r = np.array([x + 0.5, y, z + 0.5]) * unit_cell_size 
                    v = np.zeros(3)
                    #v = np.random.normal(0, np.sqrt(T), size = 3) 
                    self.particles.append(particle(r, v, m))

                    r = np.array([x + 0.5, y + 0.5, z]) * unit_cell_size 
                    v = np.zeros(3)
                    #v = np.random.normal(0, np.sqrt(T), size = 3)
                    self.particles.append(particle(r, v, m))

    # calculating force between two particles:        
    #def lennard_jones(self, i, j, coord_array):
    def lennard_jones(self, i, j):
        r_i = self.particles[i].r
        r_j = self.particles[j].r
        #r_j = self.particles[j].r + coord_array # by using coord_array we also consider interactions with dummy particles outside the boundaries
        s = np.sqrt((r_i[0] - r_j[0])**2 + (r_i[1] - r_j[1])**2 + (r_i[2] - r_j[2])**2) # calculating distance between two particles
        if np.isnan(s):
            print("Error: contains NaN values")
            sys.exit()
        # particles far apart have negligible interactions
        if s > 3:
            F = 0
        else:
            F = 24*(2/s**12 - 1/s**6)*(r_i - r_j)/(s**2)
        return F
    
    # calculating total force from all particles acting on a chosen particle:
    def total_force_particles(self, i): 
        F = np.zeros(3)
        # all the possible values that can be added to particle coordinates to create dummy particles outside boundaries:
        #boundaries = np.array(list(product([-system_size, 0, system_size], repeat=3)))
        n = len(self.particles)
        for j in range(n):
            if j != i:
                F += self.lennard_jones(i, j)
                #for k in range(boundaries.shape[0]):
                    #F += self.lennard_jones(i, j, boundaries[k])
        return F

    # system evolution for a single step:
    def verlet_evolve(self, dt, system_size):
        n = len(self.particles)
        a = np.zeros((n, 3))
        # calculate acceleration for all particles:
        for i in range(n):
            F = self.total_force_particles(i)
            a[i] = F/self.particles[i].m
        # write to file and update velocities and positions for all particles:
        for i in range(n):
            with open('md.txt', 'a') as file:
                file.write(f"Ar          {self.particles[i].r[0]:.10f}          {self.particles[i].r[1]:.10f}          {self.particles[i].r[2]:.10f}\n")
            self.particles[i].v = self.particles[i].v + 0.5*a[i]*dt
            self.particles[i].r = self.particles[i].r + self.particles[i].v*dt
            """
            # get the particles that leave the system to re-enter from the opposite side:
            for k in range(3):
                if self.particles[i].r[k] > system_size:
                    self.particles[i].r[k] = self.particles[i].r[k] % system_size
                if self.particles[i].r[k] < 0:
                    self.particles[i].r[k] = self.particles[i].r[k] % system_size
            """
        # again calculate acceleration for all particles:
        for i in range(n):       
            F = self.total_force_particles(i)
            a[i] = F/self.particles[i].m
        # update velocities for all particles:
        for i in range(n): 
            self.particles[i].v = self.particles[i].v + 0.5*a[i]*dt

    # system evolution through time:     
    def verlet_simulate(self, dt, t, unit_cell_size, lattice_dim):
        n_iter = int(t/dt)
        n = len(self.particles)
        with open('md.txt', 'w') as file:
            pass
        for i in range(n_iter):
            with open('md.txt', 'a') as file:
                file.write(f"{n}\n")
                file.write("type                    x                    y                    z\n")
            self.verlet_evolve(dt, system_size = unit_cell_size * lattice_dim)
        # write last step to file:
        with open('md.txt', 'a') as file:
            file.write(f"{n}\n")
            file.write("type                    x                    y                    z\n")
        for i in range(n):
            with open('md.txt', 'a') as file:
                file.write(f"Ar          {self.particles[i].r[0]:.10f}          {self.particles[i].r[1]:.10f}          {self.particles[i].r[2]:.10f}\n")
            
            
            
            

   
