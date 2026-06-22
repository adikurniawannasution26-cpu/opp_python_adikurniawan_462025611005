class SaldoMinimalError(Exception):
    """Exception khusus jika saldo setelah penarikan berada di bawah saldo minimal."""


class RekeningBank:
    def __init__(self, pemilik: str, saldo_awal: int, saldo_minimal: int = 0):
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.saldo_minimal = saldo_minimal

    def cek_saldo(self) -> int:
        return self.saldo

    def tarik_uang(self, jumlah: int) -> str:
        if jumlah <= 0:
            raise ValueError("Jumlah penarikan harus lebih dari 0.")

        saldo_setelah = self.saldo - jumlah
        if saldo_setelah < self.saldo_minimal:
            raise SaldoMinimalError(
                f"Saldo tidak mencukupi untuk penarikan Rp{jumlah}. "
                f"Saldo setelah penarikan Rp{saldo_setelah} berada di bawah saldo minimal Rp{self.saldo_minimal}."
            )

        self.saldo = saldo_setelah
        return f"Penarikan Rp{jumlah} berhasil. Saldo sekarang Rp{self.saldo}."


def main():
    rekening = RekeningBank(pemilik="Adi", saldo_awal=100_000, saldo_minimal=50_000)

    try:
        print("=== PENARIKAN UANG PERTAMA ===")
        pesan = rekening.tarik_uang(60_000) 
        print(pesan)
    except SaldoMinimalError as e:
        print("Error Custom:", e)
    except Exception as e:
        print("Error Umum:", e)
    finally:
        print("Proses pemeriksaan telah selesai dilakukan.\n")

    try:
        print("=== PENARIKAN UANG KEDUA ===")
        pesan = rekening.tarik_uang(40_000) 
        print(pesan)
    except SaldoMinimalError as e:
        print("Error Custom:", e)
    except Exception as e:
        print("Error Umum:", e)
    finally:
        print("Proses pemeriksaan telah selesai dilakukan.")


if __name__ == "__main__":
    main()

