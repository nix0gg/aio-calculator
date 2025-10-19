import math

#Stress
def longitudinal_stress(F, A):
    return F / A


__all__ = [name for name in globals() if not name.startswith("_")]
