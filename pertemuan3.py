class Mahasiswa:
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        
    def tampilkan_data(self):
        print(f"Nama  : {self.nama}")
        print(f"Nilai : {self.nilai}")
        
    def lulus(self):
        if self.nilai >=75:
            return "Lulus"
        else:
            return "Tidak Lulus"
        
    @staticmethod
    def hitung_grade(nilai):
        if nilai >= 90:
            return "A"
        elif nilai >= 80:
            return "B"
        elif nilai>= 70:
            return "C"
        else:
            return "D"
        
mhs1 = Mahasiswa("Adi", 85)

mhs1.tampilkan_data()
print("Status :", mhs1.lulus())

print("Grade :", Mahasiswa.hitung_grade(85))