from physics_constants import c, N_A, e
import math
def area(length, breadth):
    return length * breadth

def volume(length, breadth, height):
    return length * breadth * height

def mass_density(mass, volume):
    return mass / volume

def frequency(time_period):
    return 1 / time_period

def speed(distance, time):
    return distance / time

def acceleration(change_in_velocity, time):
    return change_in_velocity / time

def force(mass, acceleration):
    return mass * acceleration

def impulse(force, time):
    return force * time

def work(force, distance):
    return force * distance

def power(work, time):
    return work / time

def momentum(mass, velocity):
    return mass * velocity  

def pressure(force, area):
    return force / area

def strain(dimensional_change, original_dimension):
    return dimensional_change / original_dimension

def modulus_of_elasticity(stress, strain):
    return stress / strain

def surface_tension(force, length):
    return force / length
def surface_energy(energy, area):
    return energy / area
def velocity_gradient(change_in_velocity, distance):
    return change_in_velocity / distance
def pressure_gradient(change_in_pressure, distance):
    return change_in_pressure / distance
def pressure_energy(pressure, volume):
    return pressure * volume
def coefficient_of_viscosity(shear_stress, velocity_gradient):
    return shear_stress / velocity_gradient
def angular_displacement(arc,radius):
    return arc / radius
def angular_velocity(angular_displacement, time):
    return angular_displacement / time

def angular_acceleration(angular_velocity, time):
    return angular_velocity / time
def moment_of_inertia(mass, radius_gyration):
    return mass * radius_gyration**2
def angular_momentum(moment_of_inertia, angular_velocity):
    return moment_of_inertia * angular_velocity
def torque(force,distance):
    return force * distance
def angular_frequency(time_period):
    return 2 * math.pi / time_period
def hubble_constant(recession_speed, distance):
    return recession_speed / distance
def intensity_of_wave(energy,time,area):
    return (energy/time)/area
def radiation_pressure(intensity_of_wave, speed_of_light):
    return intensity_of_wave / speed_of_light
def energy_density(energy, volume):
    return energy / volume
def critical_velocity(reynold_no, coefficient_of_viscosity, density,radius):
    return (reynold_no * coefficient_of_viscosity) / (density * radius)
def escape_velocity(mass, radius, gravitational_constant):
    return math.sqrt((2 * gravitational_constant * mass) / radius)
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2
def potential_energy(mass, height, gravitational_acceleration):
    return mass * gravitational_acceleration * height
def rotational_kinetic_energy(moment_of_inertia, angular_velocity):
    return 0.5 * moment_of_inertia * angular_velocity**2
def efficiency(output_energy, input_energy):
    return (output_energy / input_energy) * 100
def angular_impulse(torque, time):
    return torque * time
def gravitational_constant(force, mass1, mass2, distance):
    return (force * distance**2) / (mass1 * mass2)
def plancks_constant(energy, frequency):
    return energy / frequency
def heat_capacity(heat_energy, temperature):
    return heat_energy / temperature
def specific_heat_capacity(heat_energy, mass, temperature):
    return heat_energy / (mass * temperature)
def latent_heat(heat_energy, mass):
    return heat_energy / mass
def thermal_expansion(change_in_dimension, original_dimension, change_in_temperature):
    return change_in_dimension / (original_dimension * change_in_temperature)
def bulk_modulus(volume, change_in_volume, change_in_pressure):
    return -change_in_pressure * volume / change_in_volume
def centripetal_acceleration(velocity, radius):
    return velocity**2 / radius
def stefan_constant(energy, temperature, area, time):
    return energy / (area * time * temperature**4)
def wien_constant(wavelength, temperature):
    return wavelength * temperature
def boltzmann_constant(energy, temperature):
    return energy / temperature
def universal_gas_constant(pressure, volume, temperature, moles):
    return (pressure * volume) / (temperature * moles)
def charge(current, time):
    return current * time
def current_density(current, area):
    return current / area
def voltage(work,charge):
    return work / charge
def resistance(voltage, current):
    return voltage / current
def capacitance(charge, voltage):
    return charge / voltage
def electrical_resistivity(resistance, length, area):
    return (resistance * area) / length
def electric_field(electrical_force, charge):
    return electrical_force / charge
def electric_flux(electric_field, area):
    return electric_field * area
def electrtic_dipole_moment(torque, electric_field):
    return torque / electric_field
def electric_intensity(potential_difference, distance):
    return potential_difference /distance 
def magnetic_flux(magnetic_field,area):
    return magnetic_field * area
def inductance(magnetic_flux, current):
    return magnetic_flux * current
def magnetic_dipole_moment(torque,magnetic_field):
    return torque / magnetic_field
def magnetic_field_strength(magnetic_moment, volume):
    return magnetic_moment / volume
def permittivity_constant(charge1, charge2, electric_force,distance):
    return (charge*charge)/4*math.pi*electric_force*(distance**2)
def permeability_constant(force, distance, current1,current2,length):
    return (2*math.pi*force*distance)/(current1*current2*length)
def refractive_index(l):
    return c/l

