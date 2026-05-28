class AkunInstagram:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__followers = 0
        
    def get_username(self):
        return self.__username
    
    def get_email(self, password):
        if password == self.__password:
            return f"Email : {self.__email}"
        else:
            return "Password salah! Tidak dapat melihat email."
        
    def get_followers(self):
        return f"Jumlah followers : {self.__followers}"
    
    def tambah_followers(self, jumlah):
        self.__followers += jumlah
        return f"Followers bertambah {jumlah}"
    
    def ganti_password(self, password_lama, password_baru):
        if password_lama == self.__password:
            self.__password = password_baru
            return "Password berhasil diganti."
        else:
            return "Password lama salah!."
    
    def ubah_email(self, password, email_baru):
        if password == self.__password:
            self.__email = email_baru
            return "Email berhasil diubah."
        else:
            return "Gagal mengubah email! Password salah."
        
akun1 = AkunInstagram("adikurniawan", "adi1106", "adi@gmail.com")

print(akun1.get_username())

print(akun1.get_email("adi1106"))

print(akun1.get_email("123"))

print()

print(akun1.tambah_followers(100))
print(akun1.get_followers())

print()

print(akun1.ganti_password("salah", "adi2006"))

print(akun1.ganti_password("adi1106", "adi2006"))

print()

print(akun1.ubah_email("adi1106", "adikur@gmail.com"))

print(akun1.ubah_email("adi2006", "adikur@gmail.com"))

print(akun1.get_email("adi2006"))

print()