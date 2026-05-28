class Mahasiswa:
    
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jursan = jurusan
        
    def tampilkan_data(self):
        print("Nama    :", self.nama)
        print("Nim     :", self.nim)
        print("Jurusan :", self.jursan)
        
mahasiswa1 = Mahasiswa("Adi Kurniawan", "462025611005", "Teknik Inforamtika")
mahasiswa2 = Mahasiswa("Dafa Muzafar", "462025611909", "AFI")

mahasiswa1.tampilkan_data()

print("----------------------------")

mahasiswa2.tampilkan_data()