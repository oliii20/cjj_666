import random

class Particle:
    def __init__(self, bounds):
        self.position = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))]
        self.velocity = [0.0 for _ in range(len(bounds))]
        self.best_position = self.position[:]
        self.best_fitness = float('inf')

    def update_velocity(self, global_best_position, w=0.5, c1=1.5, c2=1.5):
        for i in range(len(self.velocity)):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            social = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive + social

    def update_position(self, bounds):
        for i in range(len(self.position)):
            self.position[i] = self.position[i] + self.velocity[i]
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]

class PSO:
    def __init__(self, objective_function, bounds, num_particles=30, max_iter=100):
        self.objective_function = objective_function
        self.bounds = bounds
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.global_best_position = None
        self.global_best_fitness = float('inf')
        self.swarm = [Particle(bounds) for _ in range(num_particles)]

    def optimize(self):
        for _ in range(self.max_iter):
            for particle in self.swarm:
                fitness = self.objective_function(particle.position)
                if fitness < particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position[:]
                if fitness < self.global_best_fitness:
                    self.global_best_fitness = fitness
                    self.global_best_position = particle.position[:]

            for particle in self.swarm:
                particle.update_velocity(self.global_best_position)
                particle.update_position(self.bounds)

        return self.global_best_position, self.global_best_fitness

# Example usage:
if __name__ == '__main__':
    def sphere(x):
        return sum([xi**2 for xi in x])

    bounds = [(-5, 5), (-5, 5)]  # 2D problem
    pso = PSO(sphere, bounds)
    best_position, best_fitness = pso.optimize()
    print(f'Best position: {best_position}')
    print(f'Best fitness: {best_fitness}')