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

    def total_force(self):
        return 0

    def verlet_evolve(self, dt):
        a = self.total_force()/self.particles[0].m
        self.particles[0].v = self.particles[0].v + 0.5*a*dt
        self.particles[0].r = self.particles[0].r + self.particles[0].v*dt
        a = self.total_force()/self.particles[0].m
        self.particles[0].v = self.particles[0].v + 0.5*a*dt
