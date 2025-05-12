import main

class ShoppingCart:
    #method-- specific to a class and is accessed by an object?
    #(but methods and functions aren't exactly the same)

    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price: float):
        #list w/ tuples somewhere
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name, str):

        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
            break #after the item is removed it breaks the loop so as not to waste time(efficiency)

    def calculate_total(self)->float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price

        return total

    def summary(self):

        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @Ksh {price:.2f} each")

        print(f"Total: Ksh{self.calculate_total():.2f} \n")

def checkout(cart: ShoppingCart):
    cart.summary()
    print(f"Final amount: Ksh {cart.calculate_total():2f}\n")

if __name__ == "__main__":
    cart: ShoppingCart = ShoppingCart()
    cart.add_items("Apple", 50, 48.0)
    cart.add_items("Kiwi", 45, 98.0)
    cart.add_items("Mango", 40, 30.5)

    print(">>> Regular cart <<<")

    checkout(cart)
