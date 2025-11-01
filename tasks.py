class Product:
    """Клас, що описує товар у магазині."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} — {self.price:.2f} грн (в наявності: {self.quantity})"

    def is_available(self, amount: int) -> bool:
        """Перевірка, чи є достатньо товару на складі."""
        return self.quantity >= amount


class Cart:
    """Клас, що описує кошик покупця."""
    def __init__(self):
        self.items = {}  # ключ — товар, значення — кількість

    def add_product(self, product: Product, amount: int = 1):
        """Додавання товару до кошика."""
        if not product.is_available(amount):
            print(f" Недостатньо товару '{product.name}' на складі!")
            return

        self.items[product] = self.items.get(product, 0) + amount
        product.quantity -= amount
        print(f" Додано {amount} шт. товару '{product.name}' до кошика.")

    def remove_product(self, product: Product, amount: int = 1):
        """Видалення товару з кошика."""
        if product not in self.items:
            print(f" Товар '{product.name}' відсутній у кошику.")
            return
        if amount >= self.items[product]:
            product.quantity += self.items[product]
            del self.items[product]
            print(f" Товар '{product.name}' повністю видалено з кошика.")
        else:
            self.items[product] -= amount
            product.quantity += amount
            print(f" Видалено {amount} шт. товару '{product.name}'.")

    def total_price(self) -> float:
        """Підрахунок загальної вартості всіх товарів у кошику."""
        return sum(p.price * qty for p, qty in self.items.items())

    def clear_cart(self):
        """Очищення кошика (повертає товари на склад)."""
        for p, qty in self.items.items():
            p.quantity += qty
        self.items.clear()
        print(" Кошик очищено!")

    def show_cart(self):
        """Вивести вміст кошика."""
        if not self.items:
            print(" Кошик порожній.")
            return
        print("\n Вміст кошика:")
        for product, qty in self.items.items():
            print(f" - {product.name}: {qty} шт. × {product.price:.2f} грн = {product.price * qty:.2f} грн")
        print(f" Загальна сума: {self.total_price():.2f} грн\n")



if __name__ == "__main__":

    apple = Product("Яблуко", 12.5, 10)
    bread = Product("Хліб", 25.0, 5)
    milk = Product("Молоко", 30.0, 8)


    cart = Cart()


    cart.add_product(apple, 3)
    cart.add_product(bread, 2)
    cart.add_product(milk, 1)
    cart.show_cart()


    cart.remove_product(bread, 1)
    cart.show_cart()


    print(f" До сплати: {cart.total_price():.2f} грн")


    cart.clear_cart()
    cart.show_cart()
