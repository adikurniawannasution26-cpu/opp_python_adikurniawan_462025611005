# Import library
from datetime import datetime

# Definisi kelas Simaksi
class Simaksi:
    def __init__(self, nama, alamat, kapasitas):
        self.nama = nama
        self.alamat = alamat
        self.kapasitas = kapasitas
        self.daftar_pemesanan = []

    def tambah_pemesanan(self, nama, tanggal, jumlah):
        pemesanan = {
            'nama': nama,
            'tanggal': tanggal,
            'jumlah': jumlah
        }
        self.daftar_pemesanan.append(pemesanan)

    def lihat_pemesanan(self):
        return self.daftar_pemesanan

    def batalkan_pemesanan(self, tanggal):
        self.daftar_pemesanan = [pemesanan for pemesanan in self.daftar_pemesanan if pemesanan['tanggal'] != tanggal]

# Definisi kelas Pemesanan
class Pemesanan:
    def __init__(self, nama, tanggal, jumlah):
        self.nama = nama
        self.tanggal = tanggal
        self.jumlah = jumlah

    def __str__(self):
        return f"{self.nama} - {self.tanggal} - {self.jumlah}"

# Fungsi utama
def main():
    simaksi = Simaksi("Gunung Merapi", "Jl. Raya Gunung Merapi", 100)
    print("Sistem Pemesanan Tiket Simaksi Pendakian Gunung")
    while True:
        print("\nMenu:")
        print("1. Tambah Pemesanan")
        print("2. Lihat Pemesanan")
        print("3. Batal Pemesanan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            jumlah = int(input("Masukkan jumlah: "))
            simaksi.tambah_pemesanan(nama, tanggal, jumlah)
            print("Pemesanan berhasil ditambahkan!")
        elif pilihan == "2":
            print("Daftar Pemesanan:")
            for pemesanan in simaksi.lihat_pemesanan():
                print(pemesanan)
        elif pilihan == "3":
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            simaksi.batal_pemesanan(tanggal)
            print("Pemesanan berhasil dibatalkan!")
        elif pilihan == "4":
            break
        else:
            print("Menu tidak tersedia!")

if __name__ == "__main__":
    main()
# Import library
from pemesanan_tiket import Simaksi

# Fungsi utama
def main():
    simaksi = Simaksi("Gunung Merapi", "Jl. Raya Gunung Merapi", 100)
    print("Sistem Pemesanan Tiket Simaksi Pendakian Gunung")
    print("Daftar Pemesanan:")
    for pemesanan in simaksi.lihat_pemesanan():
        print(pemesanan)

if __name__ == "__main__":
    main()
# Import library
import unittest
from pemesanan_tiket import Simaksi, Pemesanan

# Fungsi test
def test_tambah_pemesanan():
    simaksi = Simaksi("Gunung Merapi", "Jl. Raya Gunung Merapi", 100)
    simaksi.tambah_pemesanan("John Doe", "2022-01-01", 2)
    assert len(simaksi.lihat_pemesanan()) == 1

def test_lihat_pemesanan():
    simaksi = Simaksi("Gunung Merapi", "Jl. Raya Gunung Merapi", 100)
    simaksi.tambah_pemesanan("John Doe", "2022-01-01", 2)
    assert len(simaksi.lihat_pemesanan()) == 1

def test_batal_pemesanan():
    simaksi = Simaksi("Gunung Merapi", "Jl. Raya Gunung Merapi", 100)
    simaksi.tambah_pemesanan("John Doe", "2022-01-01", 2)
    simaksi.batal_pemesanan("2022-01-01")
    assert len(simaksi.lihat_pemesanan()) == 0

# Fungsi test
def test_pemesanan():
    pemesanan = Pemesanan("John Doe", "2022-01-01", 2)
    assert str(pemesanan) == "John Doe - 2022-01-01 - 2"

# Fungsi test
class TestPemesananTiket(unittest.TestCase):
    def test_tambah_pemesanan(self):
        test_tambah_pemesanan()

    def test_lihat_pemesanan(self):
        test_lihat_pemesanan()

    def test_batal_pemesanan(self):
        test_batal_pemesanan()

    def test_pemesanan(self):
        test_pemesanan()

if __name__ == "__main__":
    unittest.main()