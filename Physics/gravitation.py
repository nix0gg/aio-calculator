from physics_constants import G, g
import math

def universal_gravitational_force(m1, m2, r):
    return G * (m1 * m2) / r**2

def gravitational_acceleration(m, r):
    return G * m / r**2

def escape_velocity(m, r):
    return math.sqrt(2 * G * m / r)

def orbital_velocity(m, r):
    return math.sqrt(G * m / r)

def time_period(m, r):
    return 2 * math.pi * math.sqrt(r**3 / (G * m))

def weight(m):
    return m * g

def gravitational_potential_energy(m1, m2, r):
    return -G * (m1 * m2) / r

__all__ = [name for name in globals() if not name.startswith("_")]
