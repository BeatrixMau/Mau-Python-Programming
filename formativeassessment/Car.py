class Car:
    def __init__ (self, color, size, model, speed):
        self.color=color
        self.size=size
        self.model=model
        self.speed=speed
    def info(self):
        print(f"I have a new car. It is in {self.color} and can fit {self.size} of passengers. The model of my car is {self.model} and it can go up to {self.speed}")
car_color = input("Color of the Car: ")
car_size = int(input("Size of the Car(Maximum passengers): "))
car_model = str(input("Model of the Car: "))
car_speed = input("Speed p/km: ")
car1 = Car(car_color, car_size, car_model, car_speed)   

car1.info()