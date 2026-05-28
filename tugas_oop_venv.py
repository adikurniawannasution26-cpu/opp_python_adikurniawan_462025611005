class Product:
    def __init__(self, name: str, price: int, qty: int):
        # atribut (state) milik objek
        self.name = name
        self.price = price
        self.qty = qty

    def subtotal(self) -> int:
        # behavior
        return self.price * self.qty

    def __str__(self) -> str:
        return f"{self.name} | Harga: {self.price} | Qty: {self.qty} | Subtotal: {self.subtotal()}"


class Receipt:
    def __init__(self, cashier_name: str):
        self.cashier_name = cashier_name
        self.items = []

    def add_item(self, product: Product):
        # komposisi: receipt punya banyak product
        self.items.append(product)

    def total(self) -> int:
        return sum(item.subtotal() for item in self.items)

    def print_receipt(self):
        print("\n===== STRUK BELANJA =====")
        print(f"Kasir     : {self.cashier_name}")
        print("-" * 30)
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")
        print("-" * 30)
        print(f"TOTAL BELANJA : {self.total()}")
        print("==========================\n")


def main():
    cashier = input("Masukkan nama kasir: ").strip()
    receipt = Receipt(cashier)

    n = int(input("Berapa jumlah item yang dibeli? "))

    for _ in range(n):
        name = input("Nama barang: ").strip()
        price = int(input("Harga barang: "))
        qty = int(input("Jumlah barang: "))

        product = Product(name, price, qty)
        receipt.add_item(product)

    receipt.print_receipt()


if __name__ == "__main__":
    main()

