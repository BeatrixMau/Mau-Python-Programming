class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")
    def makesound(self):
        print("Meow")
cat1_name = input("Enter the name of the first cat: ")
cat1_age = int(input("Enter the age of the first cat: "))
cat1 = Cat(cat1_name, cat1_age)

cat2_name = input("Enter the name of the second cat: ")
cat2_age = int(input("Enter the age of the second cat: "))
cat2 = Cat(cat2_name, cat2_age)

cat1.info()
cat1.makesound()

cat2.info()
cat2.makesound()
    