import numpy as np
import matplotlib.pyplot as plt
from itertools import product

"""
To do:
Add comments
Time scale?
Add a boolean variable to turn on/off boundary conditions?
Add temperature, pressure calculations, etc.
Better code structure?
Optimize?
Other gases than argon?
"""

class particle:
    def __init__ (self, mass, position, velocity):
        self.m = mass
        self.r = position
        self.v = velocity

class system:
    def __init__ (self):
        self.particles = []

    def add_particles(self, m, n, T, system_size):
        for i in range(n):
            r = np.random.uniform(low = 0, high = system_size, size = 3) # particles uniformly distributed in space
            v = np.random.normal(0, np.sqrt(T/m), size = 3) # velocities distribution
            self.particles.append(particle(m, r, v))

    # calculating force between two particles:        
    def lennard_jones(self, i, j, coord_array):
        particle_i = self.particles[i]
        particle_j = self.particles[j]
        r_i = particle_i.r
        r_j = particle_j.r + coord_array # by using coord_array we also consider interactions with dummy particles outside the boundaries
        s = np.sqrt((r_i[0] - r_j[0])**2 + (r_i[1] - r_j[1])**2 + (r_i[2] - r_j[2])**2) # calculating distance between two particles
        # condition that particles more than 3 units apart don't interact:
        if s > 3:
            F = 0
        else:
            F = 24*(2/s**12 - 1/s**6)*(r_i - r_j)/(s**2)
        return F
    
    # calculating total force from all particles acting on a chosen particle:
    def total_force_particles(self, i, n): 
        F = np.zeros(3)
        # all the possible values that can be added to particle coordinates to create dummy particles outside boundaries:
        boundaries = np.array(list(product([-1, 0, 1], repeat=3)))
        for j in range(n):
            if j != i:
                for k in range(boundaries.shape[0]):
                    F += self.lennard_jones(i, j, boundaries[k])
        return F

    # system evolution for a single step:
    def verlet_evolve(self, dt, n):
        for i in range(n):
            with open('md.txt', 'a') as file:
                file.write(f"Ar          {self.particles[i].r[0]:.10f}          {self.particles[i].r[1]:.10f}          {self.particles[i].r[2]:.10f}\n")
            F = self.total_force_particles(i, n)
            a = F/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt
            self.particles[i].r = self.particles[i].r + self.particles[i].v*dt
            # getting the particles that leave the system to re-enter from the opposite side:
            for k in [0, 1, 2]:
                if self.particles[i].r[k] > 1:
                    self.particles[i].r[k] = self.particles[i].r[k] % 1
                if self.particles[i].r[k] < 0:
                    self.particles[i].r[k] = self.particles[i].r[k] % 1 
                
            F = self.total_force_particles(i, n)
            a = F/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt
            
    def verlet_simulate(self, dt, t, n):
        n_iter = int(t/dt)
        with open('md.txt', 'w') as file:
            pass
        for i in range(n_iter):
            with open('md.txt', 'a') as file:
                file.write(f"{n}\n")
                file.write("type                    x                    y                    z\n")
            self.verlet_evolve(dt, n)
            
            
            
            

   
