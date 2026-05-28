class Kendaraan:
    
    def __init__(self):
        print("Kendaraan dibuat")
        
    def info(self):
        print("Ini adalah kendaraan")
        
class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Mobil dibuat")
        
    def info(self):
        super().info()
        print("Mobil memiliki 4 roda")
        
class Motor(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Motor dibuat")
        
    def info(self):
        super().info()
        print("Motor memiliki 2 roda")
        
class KendaraanListrik(Mobil, Motor):
    def __init__(self):
        super().__init__()
        print("Kendaraan listrik dibuat")
        
    def info(self):
        super().info()
        print("Menggunakan tenaga listrik")
        
obj = KendaraanListrik()

print("\nInformasi kendaraan:")
obj.info()

print("\nMethod Resolution Order (MRO):")
print(KendaraanListrik.__mro__)