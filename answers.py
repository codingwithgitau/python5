# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"📞 Calling {number} from {self.model}...")

    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Derived Class (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, waterproof):
        super().__init__(brand, model, storage)
        self.waterproof = waterproof

    def info(self):  # Overriding (Polymorphism / Encapsulation)
        print(f"{self.brand} {self.model} Watch | Waterproof: {self.waterproof}")

# Create objects
phone = Smartphone("Samsung", "Galaxy S23", 256)
watch = Smartwatch("Apple", "Watch Series 9", 32, True)

# Use methods
phone.info()
phone.call("0712345678")
watch.info()
watch.call("0798765432")

class Vehicle:
    def move(self):
        print("This vehicle moves")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on water...")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
