def center_of_mass(masses, positions):
    numerator = sum(masses[i] * positions[i] for i in range(len(masses)))
    denominator = sum(masses)
    return numerator / denominator

def linear_momentum(mass, velocity):
    return mass * velocity

def total_momentum(masses, velocities):
    return sum(masses[i] * velocities[i] for i in range(len(masses)))

def moment_of_inertia(masses, distances):
    return sum(masses[i] * distances[i]**2 for i in range(len(masses)))

def torque(i, alpha):
    return i * alpha

def angular_momentum(i, omega):
    return i * omega

def rotational_kinetic_energy(i, omega):
    return 0.5 * i * omega**2
