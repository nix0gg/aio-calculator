import math
g = 9.8

def work(f,d,theta):
    return f*d*math.cos(theta)
global theta
def kinetic_energy(m,v):
    return 0.5*m*(v**2)

def potential_energy(m,h):
    return m*g*h

def total_mechanical_energy(ke,pe):
    return ke+pe

def power(w,t):
    return w/t

def power_2(f,v):
    return f*v*math.cos(theta)

def work_energy_theorem(k2,k1,e):
    delta_k = k2-k1
    return (k2-k1)*e
