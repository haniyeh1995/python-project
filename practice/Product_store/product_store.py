import json
import os

class Product:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_stock(self, amount):
        self.quantity += amount
        print(f"the quantity of {self.name} updatetd. New quantity: {self.quantity}")
    
    def purchase(self, amount):
        if self.quantity >= amount :
            self.quantity -= amount
            total_price = self.price * amount
            print(f"🛒 You bought {amount} of {self.name}. Total price: {total_price} Toman")
        else:
            print(f"Not enough stock!")
    
    def product_info(self):
        print(f"📌 {self.name} | Price: {self.price} Toman | In stock: {self.quantity}")

    def to_dict(self):
        return {
            "name" : self.name ,
            "price": self.price ,
            "quantity" : self.quantity
        }
    
    @classmethod
    def from_dict(clss, data):
        return clss(data["name"], data["price"], data["quantity"])
    

# --------------------------saving methods--------------------------------

def save_products(products, filename="store.json"):
    data = [p.to_dict() for p in products]
    with open(filename, "w") as f:
        json.dump(data, f)

def load_products(filename="store.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
        return [Product.from_dict(p) for p in data]

# ---------------------------main program------------------------------------
products = load_products()
print("📦 Products loaded from file.")

while True:
    print("\n🛍 Store Menu:")
    print("1. Add Product")
    print("2. Update Stock")
    print("3. Purchase Product")
    print("4. Show All Products")
    print("5. Exit\n")

    try:
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("⚠️ Please enter a number.")
        continue

    if choice == 1:
        name = input("type your product name: \n")
        price = int(input("type it's price in Toman: \n"))
        quantity = int(input("type the quantity: \n"))
        products.append(Product(name, price, quantity))
        save_products(products)
        print(f"\n'{name}' added to inventory.")
        

    elif choice == 2:
        for idx , m in enumerate(products):
            print(f"{idx + 1}. {m.name}")
        index= int(input("which product to update? \n")) - 1
        if  0 <= index < len(products):
            amount = int(input("how many units to add? \n"))
            products[index].update_stock(amount)
        else:
            print("❌invalid selection")
        save_products(products)
    
    elif choice == 3:
        for idx , m in enumerate(products):
            print(f"{idx + 1}. {m.name}")
        index = int(input("which product to buy? \n")) - 1
        amount = int(input("how many units to buy? \n"))
        if  0 <= index < len(products):
            products[index].purchase(amount)
        else:
            print("❌invalid selection")
        save_products(products)
    
    elif choice == 4:
        if products:
            print("\n📦Product List:")
            for m in products:
                m.product_info()
        else:
            print("📭No products available.")
        
    elif choice == 5:
        print("👋 Exiting Store Menu. Goodbye!")
        break
    
    else:
        print("❌Invalid choice. Please select 1 to 6.")