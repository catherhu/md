import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
To do:
Check untis
Maybe add a boolean variable to turn on/off boundary conditions
Add temperature, pressure calculations, etc.
Improve code structure
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

    def add_particles(self, m, n, T, box_size):
        k = 1.38E-23
        for i in range(n):
            r = np.random.uniform(low = 0, high = box_size, size = 3)
            v = np.random.normal(0, np.sqrt(k*T/m), size = 3)
            self.particles.append(particle(m, r, v))
            
    def lennard_jones(self, i, j, coord_array):
        particle_i = self.particles[i]
        particle_j = self.particles[j]
        r_i = particle_i.r
        r_j = particle_j.r + coord_array
        s = np.sqrt((r_i[0] - r_j[0])**2 + (r_i[1] - r_j[1])**2 + (r_i[2] - r_j[2])**2)
        if s > 3:
            F = 0
        else:
            F = 24*(2/s**12 - 1/s**6)*(r_i - r_j)/(s**2)
        return F
    
    
    def total_force_particles(self, i, n): 
        F = np.zeros(3)
        #need a more elegant way to implement this:
        boundaries = np.array([[-1,-1,-1],[-1,-1,0],[-1,-1,1],[-1,0,-1],[-1,0,0],[-1,0,1],[-1,1,-1],[-1,1,0],[-1,1,1],
                [0,-1,-1],[0,-1,0],[0,-1,1],[0,0,-1],[0,0,0],[0,0,1],[0,1,-1],[0,1,0],[0,1,1],
                [1,-1,-1],[1,-1,0],[1,-1,1],[1,0,-1],[1,0,0],[1,0,1],[1,1,-1],[1,1,0],[1,1,1]])
        for j in range(n):
            if j != i:
                for k in range(boundaries.shape[0]):
                    F += self.lennard_jones(i, j, boundaries[k])
        return F

    def verlet_evolve(self, dt, n):
        for i in range(n):
            with open('md.txt', 'a') as file:
                file.write(f"Ar          {self.particles[i].r[0]:.10f}          {self.particles[i].r[1]:.10f}          {self.particles[i].r[2]:.10f}\n")
            F = self.total_force_particles(i, n)
            a = F/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt
            self.particles[i].r = self.particles[i].r + self.particles[i].v*dt

            #is this an accurate representation of reality?
            for k in [0, 1, 2]:
                if self.particles[i].r[k] >= 1:
                    self.particles[i].r[k] = 1E-10
                if self.particles[i].r[k] <= 0:
                    self.particles[i].r[k] = 1 - 1E-10

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
            
            
            
            

   
