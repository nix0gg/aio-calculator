import Physics.dimensional_formulas
from Physics.physics_constants import c, N_A, e, g

# ---------------------------- Basic Quantities ----------------------------
def proc_area():
    length = float(input("Enter length (L): "))
    breadth = float(input("Enter breadth (L): "))
    print("Area (L^2):", Physics.dimensional_formulas.area(length, breadth))

def proc_volume():
    length = float(input("Enter length (L): "))
    breadth = float(input("Enter breadth (L): "))
    height = float(input("Enter height (L): "))
    print("Volume (L^3):", Physics.dimensional_formulas.volume(length, breadth, height))

def proc_mass_density():
    mass = float(input("Enter mass (M): "))
    volume = float(input("Enter volume (L^3): "))
    print("Mass Density (M/L^3):", Physics.dimensional_formulas.mass_density(mass, volume))

def proc_frequency():
    time_period = float(input("Enter time period (T): "))
    print("Frequency (1/T):", Physics.dimensional_formulas.frequency(time_period))

def proc_speed():
    distance = float(input("Enter distance (L): "))
    time = float(input("Enter time (T): "))
    print("Speed (L/T):", Physics.dimensional_formulas.speed(distance, time))

def proc_acceleration():
    change_in_velocity = float(input("Enter change in velocity (L/T): "))
    time = float(input("Enter time (T): "))
    print("Acceleration (L/T^2):", Physics.dimensional_formulas.acceleration(change_in_velocity, time))

# ---------------------------- Mechanics ----------------------------
def proc_force():
    mass = float(input("Enter mass (M): "))
    acceleration = float(input("Enter acceleration (L/T^2): "))
    print("Force (MLT^-2):", Physics.dimensional_formulas.force(mass, acceleration))

def proc_impulse():
    force = float(input("Enter force (MLT^-2): "))
    time = float(input("Enter time (T): "))
    print("Impulse (MLT^-1):", Physics.dimensional_formulas.impulse(force, time))

def proc_work():
    force = float(input("Enter force (MLT^-2): "))
    distance = float(input("Enter distance (L): "))
    print("Work (ML^2T^-2):", Physics.dimensional_formulas.work(force, distance))

def proc_power():
    work = float(input("Enter work done (ML^2T^-2): "))
    time = float(input("Enter time taken (T): "))
    print("Power (ML^2T^-3):", Physics.dimensional_formulas.power(work, time))

def proc_momentum():
    mass = float(input("Enter mass (M): "))
    velocity = float(input("Enter velocity (L/T): "))
    print("Momentum (MLT^-1):", Physics.dimensional_formulas.momentum(mass, velocity))

def proc_pressure():
    force = float(input("Enter force (MLT^-2): "))
    area = float(input("Enter area (L^2): "))
    print("Pressure (ML^-1T^-2):", Physics.dimensional_formulas.pressure(force, area))

def proc_strain():
    change = float(input("Enter change in dimension (L): "))
    original = float(input("Enter original dimension (L): "))
    print("Strain (dimensionless):", Physics.dimensional_formulas.strain(change, original))

def proc_modulus_of_elasticity():
    stress = float(input("Enter stress (ML^-1T^-2): "))
    strain = float(input("Enter strain (dimensionless): "))
    print("Modulus of Elasticity (ML^-1T^-2):", Physics.dimensional_formulas.modulus_of_elasticity(stress, strain))

def proc_surface_tension():
    force = float(input("Enter force (MLT^-2): "))
    length = float(input("Enter length (L): "))
    print("Surface Tension (MT^-2):", Physics.dimensional_formulas.surface_tension(force, length))

def proc_kinetic_energy():
    mass = float(input("Enter mass (M): "))
    velocity = float(input("Enter velocity (L/T): "))
    print("Kinetic Energy (ML^2T^-2):", Physics.dimensional_formulas.kinetic_energy(mass, velocity))

def proc_potential_energy():
    mass = float(input("Enter mass (M): "))
    height = float(input("Enter height (L): "))
    print("Potential Energy (ML^2T^-2):", Physics.dimensional_formulas.potential_energy(mass, height, g))

def proc_escape_velocity():
    mass = float(input("Enter mass of body (M): "))
    radius = float(input("Enter radius (L): "))
    G = float(input("Enter gravitational constant (L^3M^-1T^-2): "))
    print("Escape Velocity (L/T):", Physics.dimensional_formulas.escape_velocity(mass, radius, G))

# ---------------------------- Electricity ----------------------------
def proc_charge():
    current = float(input("Enter current (A): "))
    time = float(input("Enter time (T): "))
    print("Charge (AT):", Physics.dimensional_formulas.charge(current, time))

def proc_current_density():
    current = float(input("Enter current (A): "))
    area = float(input("Enter area (L^2): "))
    print("Current Density (AL^-2):", Physics.dimensional_formulas.current_density(current, area))

def proc_voltage():
    work = float(input("Enter work done (ML^2T^-2): "))
    charge = float(input("Enter charge (AT): "))
    print("Voltage (ML^2T^-3A^-1):", Physics.dimensional_formulas.voltage(work, charge))

def proc_resistance():
    voltage = float(input("Enter voltage (ML^2T^-3A^-1): "))
    current = float(input("Enter current (A): "))
    print("Resistance (ML^2T^-3A^-2):", Physics.dimensional_formulas.resistance(voltage, current))

# ---------------------------- Optics and Radiation ----------------------------
def proc_refractive_index():
    speed_in_medium = float(input("Enter speed in medium (L/T): "))
    print("Refractive Index (dimensionless):", Physics.dimensional_formulas.refractive_index(speed_in_medium))

def proc_wavenumber():
    wavelength = float(input("Enter wavelength (L): "))
    print("Wavenumber (L^-1):", Physics.dimensional_formulas.wavenumber(wavelength))

# ---------------------------- Heat and Thermodynamics ----------------------------
def proc_heat_capacity():
    heat_energy = float(input("Enter heat energy (ML^2T^-2): "))
    temp_change = float(input("Enter temperature change (K): "))
    print("Heat Capacity (ML^2T^-2K^-1):", Physics.dimensional_formulas.heat_capacity(heat_energy, temp_change))

def proc_specific_heat_capacity():
    heat_energy = float(input("Enter heat energy (ML^2T^-2): "))
    mass = float(input("Enter mass (M): "))
    temp_change = float(input("Enter temperature change (K): "))
    print("Specific Heat Capacity (L^2T^-2K^-1):", 
          Physics.dimensional_formulas.specific_heat_capacity(heat_energy, mass, temp_change))

def proc_latent_heat():
    heat_energy = float(input("Enter heat energy (ML^2T^-2): "))
    mass = float(input("Enter mass (M): "))
    print("Latent Heat (L^2T^-2):", Physics.dimensional_formulas.latent_heat(heat_energy, mass))

# ---------------------------- Motion in One Dimension ----------------------------
from Physics.motion_in_one_dimension import *

def proc_velocity_1d():
    u = float(input("Enter initial velocity (L/T): "))
    t = float(input("Enter time (T): "))
    direction = input("Is direction upward? (yes/no): ").lower()
    isDirectionUp = direction == "yes"
    print("Final Velocity (L/T):", velocity(u, t, isDirectionUp))

def proc_displacement_1d():
    u = float(input("Enter initial velocity (L/T): "))
    t = float(input("Enter time (T): "))
    direction = input("Is direction upward? (yes/no): ").lower()
    isDirectionUp = direction == "yes"
    print("Displacement (L):", displacement(u, t, isDirectionUp))

def proc_max_height():
    u = float(input("Enter initial velocity (L/T): "))
    print("Maximum Height (L):", max_height(u))

def proc_time_of_flight_1d():
    u = float(input("Enter initial velocity (L/T): "))
    print("Time of Flight (T):", time_of_flight(u))

def proc_ground_strike_velocity():
    h = float(input("Enter height (L): "))
    print("Ground Strike Velocity (L/T):", ground_strike_velocity(h))

def proc_average_velocity():
    u = float(input("Enter initial velocity (L/T): "))
    v = float(input("Enter final velocity (L/T): "))
    print("Average Velocity (L/T):", average_velocity(u, v))

def proc_average_acceleration():
    u = float(input("Enter initial velocity (L/T): "))
    v = float(input("Enter final velocity (L/T): "))
    t = float(input("Enter time (T): "))
    print("Average Acceleration (L/T^2):", average_acceleration(u, v, t))

def proc_normal_force():
    m = float(input("Enter mass (M): "))
    print("Normal Force (MLT^-2):", n1(m))

def proc_normal_force_accelerated():
    m = float(input("Enter mass (M): "))
    a = float(input("Enter acceleration (L/T^2): "))
    up = input("Is acceleration upward? (yes/no): ").lower()
    if up == "yes":
        print("Normal Force (MLT^-2):", n2(m, a))
    else:
        print("Normal Force (MLT^-2):", n3(m, a))

# ---------------------------- Motion in Plane ----------------------------
from Physics.motion_in_plane import *

def proc_projectile_range():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    print("Range of Projectile (L):", range_of_projectile(u, theta))

def proc_projectile_max_height():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    print("Maximum Height of Projectile (L):", max_height(u, theta))

def proc_projectile_time_of_flight():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    print("Time of Flight (T):", time_of_flight(u, theta))

def proc_horizontal_displacement():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    t = float(input("Enter time (T): "))
    print("Horizontal Displacement (L):", horizontal_displacement(u, theta, t))

def proc_vertical_displacement():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    t = float(input("Enter time (T): "))
    print("Vertical Displacement (L):", vertical_displacement(u, theta, t))

def proc_resultant_velocity():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter angle with horizontal (degrees): "))
    t = float(input("Enter time (T): "))
    print("Resultant Velocity (L/T):", resultant_velocity(u, theta, t))

def proc_angle_of_velocity():
    u = float(input("Enter initial velocity (L/T): "))
    theta = float(input("Enter initial angle with horizontal (degrees): "))
    t = float(input("Enter time (T): "))
    print("Angle of Velocity (degrees):", angle_of_velocity(u, theta, t))

# ---------------------------- Work, Power and Energy ----------------------------
from Physics.work_power_energy import *

def proc_work_angular():
    force = float(input("Enter force (MLT^-2): "))
    distance = float(input("Enter distance (L): "))
    theta = float(input("Enter angle between force and displacement (radians): "))
    print("Work Done (ML^2T^-2):", work(force, distance, theta))

def proc_total_mechanical_energy():
    ke = float(input("Enter kinetic energy (ML^2T^-2): "))
    pe = float(input("Enter potential energy (ML^2T^-2): "))
    print("Total Mechanical Energy (ML^2T^-2):", total_mechanical_energy(ke, pe))

def proc_power_from_force():
    force = float(input("Enter force (MLT^-2): "))
    velocity = float(input("Enter velocity (L/T): "))
    theta = float(input("Enter angle between force and velocity (radians): "))
    print("Power (ML^2T^-3):", power_2(force, velocity))

def proc_work_energy_theorem():
    k2 = float(input("Enter final kinetic energy (ML^2T^-2): "))
    k1 = float(input("Enter initial kinetic energy (ML^2T^-2): "))
    e = float(input("Enter external work done (ML^2T^-2): "))
    print("Change in Kinetic Energy (ML^2T^-2):", work_energy_theorem(k2, k1, e))

def proc_efficiency():
    work_out = float(input("Enter work output (ML^2T^-2): "))
    work_in = float(input("Enter work input (ML^2T^-2): "))
    print("Efficiency (%):", efficiency(work_out, work_in))

def proc_gravitational_potential_energy():
    m1 = float(input("Enter mass of first body (M): "))
    m2 = float(input("Enter mass of second body (M): "))
    r1 = float(input("Enter initial separation (L): "))
    r2 = float(input("Enter final separation (L): "))
    print("Gravitational Potential Energy (ML^2T^-2):", 
          gravitational_potential_energy(m1, r1, r2, m2))

def proc_spring_potential_energy():
    k = float(input("Enter spring constant (MT^-2): "))
    x = float(input("Enter displacement from equilibrium (L): "))
    print("Spring Potential Energy (ML^2T^-2):", spring_potential_energy(k, x))

def proc_spring_kinetic_energy():
    k = float(input("Enter spring constant (MT^-2): "))
    x = float(input("Enter current displacement (L): "))
    xmax = float(input("Enter maximum displacement (L): "))
    print("Spring Kinetic Energy (ML^2T^-2):", kinetic_energy_spring(k, x, xmax))

# ---------------------------- Mechanical Properties of Solids ----------------------------
from Physics.mechanical_properties_solids import *

def proc_longitudinal_stress():
    force = float(input("Enter force (MLT^-2): "))
    area = float(input("Enter cross-sectional area (L^2): "))
    print("Longitudinal Stress (ML^-1T^-2):", longitudinal_stress(force, area))

# ---------------------------- Gravitation ----------------------------
from Physics.gravitation import *

def proc_gravitational_force():
    m1 = float(input("Enter mass of first body (M): "))
    m2 = float(input("Enter mass of second body (M): "))
    r = float(input("Enter distance between centers (L): "))
    print("Gravitational Force (MLT^-2):", universal_gravitational_force(m1, m2, r))

def proc_gravitational_acceleration():
    m = float(input("Enter mass of the body (M): "))
    r = float(input("Enter distance from center (L): "))
    print("Gravitational Acceleration (LT^-2):", gravitational_acceleration(m, r))

def proc_orbital_velocity():
    m = float(input("Enter mass of central body (M): "))
    r = float(input("Enter orbital radius (L): "))
    print("Orbital Velocity (LT^-1):", orbital_velocity(m, r))

def proc_orbital_period():
    m = float(input("Enter mass of central body (M): "))
    r = float(input("Enter orbital radius (L): "))
    print("Orbital Period (T):", time_period(m, r))

def proc_weight():
    m = float(input("Enter mass (M): "))
    print("Weight (MLT^-2):", weight(m))

def proc_gravitational_pe():
    m1 = float(input("Enter mass of first body (M): "))
    m2 = float(input("Enter mass of second body (M): "))
    r = float(input("Enter distance between centers (L): "))
    print("Gravitational Potential Energy (ML^2T^-2):", gravitational_potential_energy(m1, m2, r))
