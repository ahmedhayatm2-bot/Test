# 2. Simple Grocery Cart Checkout
# Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.
# Skills practiced: dictionaries, loops, input(), math operations, formatting, error handling
shopping_list = { 
            "meat":  12.99,
            "milk":  3.00,
            "water": 2.99,
            "bread": 2.99

}

print("\n Grocery items ")

for key, value in shopping_list.items():
    print(key, ":", value)

cart = {}

while True:
 checkout_cart = input("please enter an item or enter 'checkout' to exit: ").lower().strip()
 
 if checkout_cart.replace(" ", "") == "checkout":
    break
 
 if checkout_cart in shopping_list:

   while True:
      quantity = (input("How  many?: ")).strip()

      if quantity.isdigit():
       quantity = int(quantity)

       if quantity > 0:
         cart[checkout_cart] = quantity
         break
     
       else:
        print("Please enter a valid number which is atleast 1: ")
        continue
   

   print(cart)

 else:
    print("Invlaid item please enter a valid item: ")

print("\n---Final Bill---")

for products, quantity in cart.items():
   price = shopping_list[products]
   subtotal = price * quantity
   print(products, quantity, f"$ {price:.2f}", f"subtottal: $ {subtotal:.2f}")
         
