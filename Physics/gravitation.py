import math
G = 6.674e-11
g = 9.8

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

