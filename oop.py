# sınıflar (class)
# özellikler

class Car():
    #constructor
    def __init__(self,model,year=2025): # ilgili obje üretildiği an çalışır
        self.__model = model
        self.year = year

    def start(self): #self -> classın kendisini ifade eder.
        print(f"{self.__model} {self.year} arabası başlatılıyor.")

    def increase_speed(self, amount):
        print(f"Hız artırılıyor: {amount}")

    def set_model(self,model): # salt-yazılabilir
        if len(model) < 2:
            print("Model ismi 2 haneden kısa olamaz")
            return
        self.__model = model
    def get_model(self): # salt-okunur
        return self.__model


car1 = Car("Toyota") # Instance (örnek)i
car1.set_model("a")
car1.start()
car1.increase_speed(10)

car2 = Car("Hyundai",2010)
car2.start()
# Constructor (YAPICI METHOD)

# Kalıtım (Inheritance)

class Truck():
    def __init__(self,model):
        self.model = model

    def start(self):
        print(f"{self.model} başlatılıyor..")


