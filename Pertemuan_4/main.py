class Kendaraan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        
    def __str__(self):
        return f"Kendaraan: {self.nama} | Harga: ${self.harga}"
    
    def __eq__(self, other):
        return self.harga == other.harga
    
    def __it__(self, other):
        return self.harga < other.harga
    
    def __gt__(self, other):
        return self.harga > other.harga
     
kndrn1 = Kendaraan("Mobil BMW", 20000)
kndrn2 = Kendaraan("Motor Harley", 10000)
kndrn3 = Kendaraan("Mobil SupraMk5", 20000)

print(kndrn1)
print(kndrn2)
print(kndrn3)

print("\n=== Hasil Perbandingan ===")

print(f"Apakah harga {kndrn1.nama} == {kndrn3.nama}? {kndrn1 == kndrn3}")

print(f"Apakah harga {kndrn2.nama} < {kndrn2}? {kndrn2 < kndrn1}")

print(f"Apakah harga {kndrn1.nama} > {kndrn2.nama}? {kndrn1 > kndrn2}")