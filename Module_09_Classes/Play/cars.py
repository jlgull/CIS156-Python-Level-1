#!/bin/python3
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

class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        # ... This line will cause error until method is implemented
        return (f"{car.year} {car.make} {car.model}: \n  Mileage: {car.miles:,}\n"
                f"  Sticker price: ${car.price:,}")


cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)
print()
print()


class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False


workday = Duration(8, 15)
monday_time = Duration(9, 0)
tuesday_time = Duration(8, 45)
wednesday_time = Duration(6, 15)

print(monday_time < workday)
print(tuesday_time < workday)
print(wednesday_time < workday)
print(monday_time < wednesday_time)

# End of program
