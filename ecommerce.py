class Product:
    def __init__ (self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, stock={self.stock}"
class Customer:
    def __init__ (self,customer_id,name,email):
        self.customer_id=customer_id
        self.name=name
        self.email=email
    def __repr__(self):
        return f"Customer(id={self.customer_id},name={self.name},email={self.email})"
class OrderItem:
    def __init__(self,product,quantity):
        self.product=product
        self.quantity=quantity
    def __repr__(self):
        return f"Order Item={self.product.name},quantity={self.quantity},total={self.total_price()}"
    def total_price(self):
        return self.product.price*self.quantity
class Order:
    def __init__(self,order_id,customer):
        self.order_id=order_id
        self.customer=customer
        self.items=[]
        self.total=0
    def add_item(self,product,quantity):
        if product.stock>=quantity:
            self.items.append(OrderItem(product,quantity))
            self.total += product.price*quantity
            product.stock-=quantity
            print(f"Added {quantity} of {product.name} to order {self.order_id}.")
        else:
            print(f"Not enough stock for {product.name}. Only {product.stock} left.")
    def __repr__(self):
        return f"Order(id={self.order_id},customer={self.customer.name},total={self.total})"
class Payment:
    def __init__(self,order,amount):
        self.order=order
        self.amount=amount
    def process_payment(self):
        if self.amount>=self.order.total:
            print(f"Payment of ${self.amount} proceeded for order {self.order.order_id}.")
            return True
        else:
            print(f"Payment of ${self.amount} is insufficient for order {self.order.order_id}. Total is ${self.order.total}.")
            return False
class ECommerceSystem:
    def __init__(self):
        self.products={}
        self.customers={}
        self.orders={}
        self.next_order_id=1
    def add_product(self,product_id,name,price,stock):
        if product_id not in self.products:
            self.products[product_id]=Product(product_id,name,price,stock)
            print(f"Product {name} added.")
        else:
            print(f"Product ID {product_id} alreasy exists")
    def register_customer(self,customer_id,name,email):
        if customer_id not in self.customers:
            self.customers[customer_id]=Customer(customer_id,name,email)
            print(f"Customer {name} registered")
        else:
            print(f"Customer ID {customer_id} already exists")
    def place_order(self,customer_id):
        if customer_id in self.customers:
            order_id=self.next_order_id
            order=Order(order_id,self.customers[customer_id])
            self.orders[order_id]=order
            self.next_order_id += 1
            print(f"Order {order_id} placed by {self.customers[customer_id].name}.")
        else:
            print(f"Customer ID {customer_id} not found")
            return None
    def process_payment(self,order_id,amount):
        if order_id in self.orders:
            order=self.orders[order_id]
            payment=Payment(order,amount)
            if payment.process_payment():
                print(f"Order {order_id} completed.")
                return True
            else:
                print(f"order ID {order_id} not found")
                return False
    def list_products(self):
        print("Available Products:")
        for product in self.products.values():
            print(product)
    def list_customers(self):
        print("Registered Customers:")
        for customer in self.customers.values():
            print(customer)
    def list_orders(self):
        print("Orders:")
        for order in self.orders.values():
            print(order)
def main():
    system=ECommerceSystem()
    while True:
        print("\nE-Commerce System Menu")
        print("1.Add Product")
        print("2.Register Customer")
        print("3.Place Order")
        print("4.Process Payment")
        print("5.List Products")
        print("6.List Customers")
        print("7.List Orders")
        print("8.EXIT")
        choice = input("Enter your choice:")
        if choice=='1':
            product_id=input("Enter product ID")
            name=input("Enter product name")
            price=float(input("Enter product price"))
            stock=int(input("Enter product stock"))
            system.add_product(product_id,name,price,stock)
        elif choice=='2':
            customer_id=input("Enter customer ID")
            name=input("Enter customer name")
            email=input("Enter customer email")
            system.register_customer(customer_id,name,email)
        elif choice=='3':
            customer_id=input("Enter customer ID")
            order=system.place_order(customer_id)
            if order:
                while True:
                    product_id=input("Enter product ID to add to order(or 'done' to finish)")
                    if product_id=='done':
                        break
                    if product_id in system.products:
                        quantity=int(input("Enter quantity"))
                        order.add_item(system.products[product_id],quantity)
                    else:
                        print(f"Product ID {product_id} not found")
        elif choice=='4':
            order_id=int(input("Enter order ID"))
            amount=float(input("Enter payment amount"))
            system.process_payment(order_id,amount)
        elif choice=='5':
            system.list_products()
        elif choice=='6':
            system.list_customers()
        elif choice=='7':
            system.list_orders()
        elif choice=='8':
            print("Exiting the System")
            break
        else:
            print("Invalid choice. Please Try Again")
if __name__ =="__main__":
    main()
