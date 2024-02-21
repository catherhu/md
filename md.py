class particle:
    def __init__ (self, mass, position, velocity):
        self.m = mass
        self.r = position
        self.v = velocity

class system:
    def __init__ (self, n_particles):
        self.n = n_particles
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)
