"""
class Person():
    def speak(self):
        print("I tolking")

p1 = Person()
p1.speak()
p2 = Person()
p2.speak()        
"""
"""
car = {
    'make': 'Honda',
    'model': 'Accord',
    'odometer': 0,
    'year': 2008
}

def go_car(car, km):
    odometer = car.get('odometer')
    car['odometer'] = odometer + km
    return car
old_car = go_car(car, 120)
print(old_car)

old_car = go_car(car, 15)
print(old_car)
"""
"""
class Car:
    def __init__(self, auto_owner, auto_make, auto_model, prod_year):
        self.owner = auto_owner
        self.make = auto_make
        self.model = auto_model
        self.year = prod_year
        self.odometer = 0

    def go(self, km):
        self.odometer = self.odometer + km
        print("whooooooooom!!!!")

new_car = Car("Isa", "Toyota", "Camry", 2020)
print(new_car.odometer)
new_car.go(368)
print("Isas car odometer", new_car.odometer)

car_new =  Car('Doku', 'Mercedes', 's-class', 2020)
print("Dokus car odometer", car_new.odometer)
car_new.go(240)
print(car_new.odometer)
"""

# class Laptop():
#     def __init__(self,name):
#         self.name = name

#     def turn_on(self):
#         print(f'Noutbuk {self.name} vkluchen')
#         print(self.name)

# apple_mac = Laptop("MacBook Pro")            
# apple_mac.turn_on()

# dell =  Laptop("Dell Pro")
# dell.turn_on()

# Acer = Laptop("Acer Pro")
# Acer.turn_on()
"""
class Hello:
    def __init__(self, name):
        self.name = name
        self.say_hello()
    def say_hello(self):
        print(f" Salam {self.name}")

# names = ['isa', 'kuba', 'doku', 'joni']
# for object_ in names:
#     Hello(object_)        

text = ""
# while text != "q":
#     text = input("Write name: ")
#     Hello(text)

while True:
    text = input("Write name: ")
    if text == "q":
        break
    Hello(text)    
"""     
