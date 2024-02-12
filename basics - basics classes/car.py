class Car:
    wheels = 4 # class variable dla kazdy w klasie ma
    def __init__(self, make, model, year, color):
        self.make = make # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("this " + self.model +" is dribig")
    def stop(self):
        print("this " + self.model +" is stopped")