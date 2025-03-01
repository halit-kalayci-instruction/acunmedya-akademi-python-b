class Vehicle():
    def __init__(self, model):
        self.model = model
    def start(self):
        print(f"{self.model} aracı çalıştırılıyor..")

class Car(Vehicle):
    def some_car_function(self):
        print("car function")
    def start(self): # method overriding -> Polymporhism (ARAŞTIRMA)
        print("Araba başlatılıyor.")

class Truck(Vehicle):
    def __init__(self,model,capacity):
        super().__init__(model)
        self.capacity = capacity

    def load_weight(self):
        print("Kamyonete yükleniyor..")

car1 = Car("Toyota")
car1.start()
car1.some_car_function()

truck1 = Truck("Scania", 500)
truck1.start()
truck1.load_weight()