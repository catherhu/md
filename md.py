import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
To do:
Find way to test code
Add temperature, pressure calculations, etc.
Add periodic boundary conditions
Visualization?
Other gases than argon
Improve code structure
"""

class particle:
    def __init__ (self, mass, position, velocity):
        self.m = mass
        self.r = position
        self.v = velocity

class system:
    def __init__ (self):
        self.particles = []

    def add_particles(self, m, n, T, V):
        k = 1.38E-23
        for i in range(n):
            r = np.random.uniform(low = 0, high = V, size = 3)
            v = np.random.normal(0, np.sqrt(k*T/m), size = 3)
            self.particles.append(particle(m, r, v))

    #def add_boundary_conditions(self)

    def lennard_jones(self, i, j):
        eps = 1
        sig = 1
        particle_i = self.particles[i]
        particle_j = self.particles[j]
        r_i = particle_i.r
        r_j = particle_j.r
        s = np.sqrt((r_i[0] - r_j[0])**2 + (r_i[1] - r_j[1])**2 + (r_i[2] - r_j[2])**2)
        F = 24*eps*(2*(sig/s)**6 - (sig/s)**12)*(r_i - r_j)/(s**2)
        return F
    
    def total_force_particles(self, i, n):
        F = np.zeros(3)
        for j in range(n):
            if j != i:
                F += self.lennard_jones(i, j)
        return F

    def verlet_evolve(self, dt, n):
        for i in range(n):
            F = self.total_force_particles(i, n)
            a = F/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt
            self.particles[i].r = self.particles[i].r + self.particles[i].v*dt
            F = self.total_force_particles(i, n)
            a = F/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt

    def verlet_simulate(self, dt, t, n):
        n_iter = int(t/dt)
        for i in range(n_iter):
            self.verlet_evolve(dt, n)

   
