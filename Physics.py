# Inputs are optimized for Kg and G while time is optimized for hours and minutes.

# basic Physics calculator
#########

class Classic_Physics_Calculator(object):

    def speed(self):

        """ Function calculates the speed of an object from given inputs"""

        distance_input= int(input("What is the distance"))
        distance = distance_input
        time_input = int(input("how long did it take to get there"))
        time= time_input
        time_minute = time_input / 60
        speed = distance / time
        speed_min = distance / time_minute
        conversion = input("Is the time measured in hours or minutes? if hours please enter hours, if minutes please enter min")

        if conversion == "hours":
            print("The speed is " + '' + str(speed))
        else:
            print("The speed is"+ ' ' + str(speed_min ))


    def acceleration(self):

        """Calculates the acceleration of an object """


        initial_velocity_input = int(input("What is the initial velocity"))
        initial_velocity = initial_velocity_input
        final_velocity_input = int(input("What is the distance"))
        final_velocity = final_velocity_input
        initial_time_input = int(input("What is the initial time"))
        initial_time = initial_time_input
        final_time_input = int(input("What is the final time"))
        final_time = final_time_input

        acceleration = (final_velocity - initial_velocity) / (final_time - initial_time)

        print (" the acceleration is " + " " + str(acceleration))


    def weight(self):

        """ calculates the weight of an object"""


        mass_input = int(input("what is the mass of the object"))
        mass = mass_input
        mass_g = mass_input / 1000
        earth_gravity = 9.80665
        weight = mass * earth_gravity
        weight_g = mass_g * earth_gravity
        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the weight of the object is " + '' + str(weight))
        else:
            print(" The weight of the object is " + "" + str(weight_g))


    def momentum(self):

        """ calculates the momentum of an object"""

        mass_input = int(input("what is the mass of the object"))
        mass = mass_input
        mass_g = mass_input / 1000
        velocity_input= int(input("what is the velocity of the object"))
        velocity = velocity_input

        momentum = mass * velocity
        momentum_g = mass_g * velocity
        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the momentum of the object is " + '' + str(momentum))
        else:
            print("the momentum of the object is " + '' + str(momentum_g))



    def kenetic_energy(self):

        """ calculates the kenetic energy of an object"""

        mass_input = int(input("what is the mass of the object"))
        mass = mass_input
        mass_g = mass_input / 1000
        velocity_input = int(input("what is the velocity of the object"))
        velocity = velocity_input
        velocity_squared = velocity ** 2

        kenetic_energy_portion = mass * velocity_squared
        kenetic_energy_portion_g = mass_g * velocity_squared

        kenetic_energy = kenetic_energy_portion / 2
        kenetic_energy_g = kenetic_energy_portion_g / 2

        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the Kenetic Energy of the object is " + '' + str(kenetic_energy))
        else:
            print("the Kenetic Energy of the  object is " + '' + str(kenetic_energy_g))


    def power(self):

        """ calculates the power of an object"""

        work_input = int(input("what is the unit of work for this object"))
        work = work_input
        time_input = int(input("what is te unit of time for this object"))
        time = time_input
        power = work/time

        print (" the amount of power is " + '' + str(power))


    def density(self):

        """ calculates the density of an object"""

        mass_input = int(input("what is the mass of the object"))
        mass = mass_input
        mass_g = mass_input
        volume_input = int(input("what is the volume of the object"))
        volume = volume_input

        density = mass / volume
        density_g = mass_g / volume
        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the Density of the object is " + '' + str(density))
        else:
            print("the Density of the object is " + '' + str(density_g))


    def force(self):

        """ calculates the force of an object"""

        mass_input = int(input("what is the mass of the object"))
        mass_kg = mass_input
        mass_g = mass_input / 1000
        accel_input = int(input("what is the acceleration of the object"))
        acceleration = accel_input

        force = mass_kg * acceleration
        force_g =mass_g * acceleration
        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the force of the object is " + '' + str(force))
        else:
            print("the force of the object is " + '' + str(force_g))


    def gravitational_potential_energy(self):

        """ calculates the GPE of an object"""

        mass_input = int(input("what is the mass of the object"))
        mass = mass_input
        mass_g = mass_input / 1000
        earth_gravity = 9.80665
        height_input = int(input("what is the height of the object"))
        height = height_input


        GPE = mass * earth_gravity * height
        GPE_g = mass_g * earth_gravity * height
        conversion = input("Is the mass measured in kg or g? if kg please enter kg, if g please enter g")

        if conversion == "kg":
            print("the Potential Energy is " + '' + str(GPE))
        else:
            print("the Potential Energy is " + '' + str(GPE_g))




class Thermal_Physics_Calculator(object):

    def change_in_enthalpy(self):

        change_of_energy_input = int(input(str.lower("what is the change of energy?")))
        change_of_energy = change_of_energy_input
        pressure_input = int(input("what is the pressure?"))
        pressure = pressure_input
        change_of_volume_input= int(input("what is the change in volume"))
        change_of_volume= change_of_volume_input

        enthalpy = change_of_energy + change_of_volume * pressure

        print("the change in enthalpy is" + " " + str(enthalpy))






def main():
    physics = Classic_Physics_Calculator()
    print ("what would you like to solve for?")
    directory = input("The list is: \n speed, \n acceleration, \n weight, \n momentum, \n kenetic energy, \n power, \n density, \n force,\n gravitational potential energy")


    if directory == "speed":
        physics.speed()
    elif directory == "acceleration":
        physics.acceleration()
    elif directory == "weight":
        physics.weight()
    elif directory == "momentum":
        physics.momentum()
    elif directory == "kenetic energy":
        physics.kenetic_energy()
    elif directory == "power":
        physics.power()
    elif directory == "density":
        physics.density()
    elif directory == "force":
        physics.force()
    elif directory == "gravitational potential energy":
        physics.gravitational_potential_energy()

    else:
        print("there was some error, please type in the option again")
        main()

main()
