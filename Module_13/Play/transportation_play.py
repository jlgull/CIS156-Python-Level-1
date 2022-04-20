#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

#
# Define functions
#
class TransportMode:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def info(self):
        print(f'{self.name} can go {self.speed} mph.')

class Airplane(TransportMode):
    def __init__(self, name, speed):
        TransportMode.__init__(self, name, speed)
        self.fuel_gal = 0
        self.passenger_count = 0

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def fly(self, distance):
        time_2_fly = distance / self.speed

    def num_passangers(self, num):
        self.passenger_count += num

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        TransportMode.__init__(self, name, speed)
        self.mpg = mpg
        self.fuel_gal = 0

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print(f'{self.fuel_gal:f} gallons remaining.')

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        MotorVehicle.__init__(self, name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')


scooter = MotorCycle('Vespa', 55, 40)
dirtbike = MotorCycle('KX450F', 80, 25)
jetplane = Airplane('Boeing', 550)

jetplane.info()
scooter.info()
dirtbike.info()

choice = input('Select scooter (s), dirtbike (d) or jet (a): ')
bike = scooter if (choice == 's') else dirtbike if (choice == 'd') else jetplane

menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
command = input(menu)
while command != 'q':
    if command == 'f':
        fuel = int(input('Enter amount: '))
        bike.add_fuel(fuel)
    elif command == 'g':
        distance = int(input('Enter distance: '))
        bike.drive(distance)
    elif command == 'w':
        bike.wheelie()
    elif command == 'q':
        break
    else:
        print('Invalid command.')

    command = input(menu)



# End of program
