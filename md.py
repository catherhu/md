import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class particle:
    def __init__ (self, mass, position, velocity):
        self.m = mass
        self.r = position
        self.v = velocity

class system:
    def __init__ (self):
        self.particles = []

    def add_particles(self, m, n):
        for i in range(n):
            r = np.random.uniform(low = -1, high = 1, size = 3)
            v = np.random.uniform(low = -1, high = 1, size = 3)
            self.particles.append(particle(m, r, v))

    def total_force(self):
        return 0

    def verlet_evolve(self, dt, n):
        for i in range(n):
            a = self.total_force()/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt
            self.particles[i].r = self.particles[i].r + self.particles[i].v*dt
            a = self.total_force()/self.particles[i].m
            self.particles[i].v = self.particles[i].v + 0.5*a*dt

    def verlet_simulate(self, dt, t, n):
        n_iter = int(t/dt)
        for i in range(n_iter):
            self.verlet_evolve(dt, n)

   
