import math
stress = 0
strain = 0
#Stress
def longitudinal_stress(F, A):
    return F / A


#Strain
def shearing_strain(delta_x,L):
    return delta_x / L
def longitudinal_strain(delta_L, L):
    return delta_L / L
def volumetric_strain(delta_V, V):
    return delta_V / V

#Young's Modulus
def youngs_modulus(stress, strain):
    return stress / strain
def elongation(longitudinal_strain, L):
    return longitudinal_strain * L / youngs_modulus(stress, strain)


__all__ = [name for name in globals() if not name.startswith("_")]
