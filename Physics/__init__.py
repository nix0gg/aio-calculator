# Physics/__init__.py

from .conversion_factors import *
from .dimensional_formulas import *
from .gravitation import *
from .laws_of_motion import *
from .mechanical_properties_solids import *
from .motion_in_one_dimension import *
from .motion_in_plane import *
from .physics_constants import *
from .system_of_particles import *
from .work_power_energy import *

__all__ = [
    # Core physics areas
    *conversion_factors.__all__,
    *dimensional_formulas.__all__,
    *gravitation.__all__,
    *laws_of_motion.__all__,
    *mechanical_properties_solids.__all__,
    *motion_in_one_dimension.__all__,
    *motion_in_plane.__all__,
    *physics_constants.__all__,
    *system_of_particles.__all__,
    *work_power_energy.__all__,
]
