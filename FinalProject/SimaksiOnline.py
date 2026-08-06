from abc import ABC, abstractmethod

class Pendaftaran(ABC):
    
    @abstractmethod
    def ProsesRegistrasi(self) -> bool:
        pass
        
    @abstractmethod
    def ValidasiData(self) -> bool:
        pass



class Pendaki(Pendaftaran):
    def __init__(self, namaLengkap: str, email: str, noTelepon: str, daerahAsal: str, tanggalLahir: str, noTeleponRumah: str):
        # Encapsulation: Atribut diset privat (menggunakan __)
        self.__namaLengkap = namaLengkap
        self.__email = email
        self.__noTelepon = noTelepon
        self.__daerahAsal = daerahAsal
        self.__tanggalLahir = tanggalLahir
        self.__noTeleponRumah = noTeleponRumah

    # Getter dan Setter
    @property
    def namaLengkap(self): return self.__namaLengkap
    @namaLengkap.setter
    def namaLengkap(self, value): self.__namaLengkap = value

    @property
    def email(self): return self.__email
    @email.setter
    def email(self, value): self.__email = value

    @property
    def noTelepon(self): return self.__noTelepon
    @noTelepon.setter
    def noTelepon(self, value): self.__noTelepon = value

    @property
    def daerahAsal(self): return self.__daerahAsal
    @daerahAsal.setter
    def daerahAsal(self, value): self.__daerahAsal = value

    @property
    def tanggalLahir(self): return self.__tanggalLahir
    @tanggalLahir.setter
    def tanggalLahir(self, value): self.__tanggalLahir = value

    @property
    def noTeleponRumah(self): return self.__noTeleponRumah
    @noTeleponRumah.setter
    def noTeleponRumah(self, value): self.__noTeleponRumah = value

    # Method dari Class Diagram
    def inputData(self):
        return {
            "Nama": self.__namaLengkap,
            "Email": self.__email,
            "Telepon": self.__noTelepon,
            "Asal": self.__daerahAsal,
            "Lahir": self.__tanggalLahir,
            "Telp Rumah": self.__noTeleponRumah
        }

    def tampilData(self):
        print(f"Nama Lengkap         : {self.__namaLengkap}")
        print(f"Email                : {self.__email}")
        print(f"Nomor Telepon        : {self.__noTelepon}")
        print(f"Daerah Asal          : {self.__daerahAsal}")
        print(f"Tanggal Lahir        : {self.__tanggalLahir}")
        print(f"Nomor Telepon Rumah  : {self.__noTeleponRumah}")

    # Implementasi Abstraction Method
    def ValidasiData(self) -> bool:
        return bool(self.__namaLengkap and self.__email and self.__noTelepon)

    def ProsesRegistrasi(self) -> bool:
        return self.ValidasiData()


# Inheritance: Pendaki Reguler
class PendakiReguler(Pendaki):
    def __init__(self, namaLengkap: str, email: str, noTelepon: str, daerahAsal: str, tanggalLahir: str, noTeleponRumah: str):
        super().__init__(namaLengkap, email, noTelepon, daerahAsal, tanggalLahir, noTeleponRumah)


# Inheritance: Pendaki Kelompok
class PendakiKelompok(Pendaki):
    def __init__(self, namaLengkap: str, email: str, noTelepon: str, daerahAsal: str, tanggalLahir: str, noTeleponRumah: str, jumlahAnggota: int):
        super().__init__(namaLengkap, email, noTelepon, daerahAsal, tanggalLahir, noTeleponRumah)
        self.jumlahAnggota = jumlahAnggota
    
class Gunung:
    def __init__(self, namaGunung: str, kuotaPendakian: int = 100):
        self.namaGunung = namaGunung
        self.kuotaPendakian = kuotaPendakian

    def pilihGunung(self):
        return self.namaGunung
    
class Logistik:
    def __init__(self):
        self.daftarLogistik = []

    def tambahLogistik(self, item: str):
        self.daftarLogistik.append(item)

    def tampilLogistik(self):
        if not self.daftarLogistik:
            return "Tidak ada logistik tercatat"
        return ", ".join(self.daftarLogistik)

import random


class Tiket:
    def __init__(self, tanggalPendakian: str):
        self.nomorTiket = f"TKT-{random.randint(1000, 9999)}"
        self.tanggalPendakian = tanggalPendakian

    def konfirmasiData(self, pendaki: Pendaki) -> bool:
        return pendaki.ProsesRegistrasi()

    # Polymorphism: Output menyesuaikan jenis objek pendaki yang masuk
    def cetakTiket(self, pendaki: Pendaki, gunung: Gunung, logistik: Logistik):
        print("\n==========================================")
        print("          SISTEM SIMAKSI ONLINE           ")
        print("==========================================")
        print(f"Nomor Tiket       : {self.nomorTiket}")
        print(f"Tanggal Pendakian : {self.tanggalPendakian}")
        print(f"Gunung Tujuan     : {gunung.pilihGunung()}")
        print("------------------------------------------")
        
        # Cetak data dasar pendaki
        pendaki.tampilData()
        
        # Polimorfisme penentuan jenis tiket kelompok / reguler
        if isinstance(pendaki, PendakiKelompok):
            print(f"Jenis Tiket       : Tiket Pendaki Kelompok")
            print(f"Jumlah Anggota    : {pendaki.jumlahAnggota} Orang")
        else:
            print(f"Jenis Tiket       : Tiket Pendaki Reguler")
            
        print(f"Daftar Logistik   : {logistik.tampilLogistik()}")
        print("==========================================\n")



def main():
    # 1. Menampilkan Judul Sistem
    print("==========================================")
    print("          SISTEM SIMAKSI ONLINE           ")
    print("==========================================")
    
    # 2. Pendaftaran Biodata Pendaki
    nama = input("Nama Lengkap        : ")
    email = input("Email               : ")
    telp = input("Nomor Telepon       : ")
    asal = input("Daerah Asal         : ")
    lahir = input("Tanggal Lahir       : ")
    telp_rumah = input("No. Telepon Rumah   : ")
    
    print("\nPilih Jenis Pendakian:")
    print("1. Reguler / Solo")
    print("2. Kelompok")
    pilihan = input("Masukkan pilihan (1/2): ")
    
    if pilihan == "2":
        jumlah = int(input("Masukkan Jumlah Anggota Kelompok: "))
        pendaki = PendakiKelompok(nama, email, telp, asal, lahir, telp_rumah, jumlah)
    else:
        pendaki = PendakiReguler(nama, email, telp, asal, lahir, telp_rumah)

    # 3. Pemilihan Gunung Tujuan
    nama_gunung = input("\nMasukkan Gunung Tujuan: ")
    gunung = Gunung(nama_gunung)

    # 4. Pemilihan Tanggal Pendakian
    tanggal = input("Tanggal Keberangkatan (DD-MM-YYYY): ")
    tiket = Tiket(tanggal)

    # 5. Pengisian Form Logistik
    logistik = Logistik()
    print("\nMasukkan logistik yang dibawa (ketik 'selesai' jika sudah):")
    while True:
        item = input("- Nama Peralatan / Logistik: ")
        if item.lower() == 'selesai':
            break
        if item:
            logistik.tambahLogistik(item)

    # 6. Konfirmasi dan Ringkasan Tiket
    print("\n[Sistem] Melakukan validasi dan verifikasi data")
    if tiket.konfirmasiData(pendaki):
        tiket.cetakTiket(pendaki, gunung, logistik)
    else:
        print("\n[Error] Proses pendaftaran gagal. Mohon periksa kembali data Anda!")

if __name__ == "__main__":
    main()