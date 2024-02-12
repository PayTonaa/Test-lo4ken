from car import Car


car_1 = Car('cheavy', 'impala', '2003', 'blue')
car_2 = Car('ford', 'escort', '1999', 'black')
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)


car_1.drive()
car_2.stop()

car_1.wheels = 2

Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)