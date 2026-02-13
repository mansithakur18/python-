menu ={
    "pizza": 150,
    "burger": 90,
    "fries": 60,
    "sandwitch": 50,
    "coffee": 40
}

#greet

print("Welcome to MS restaurant")
print("Pizza : Rs.40\nBurger: Rs.90\nFries: Rs.60\nSandwitch: Rs.50\nCoffee: Rs.40")

order_total = 0

item_1 =input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")
    
another_item = input("Do you want to add another item? (yes/no) : ")
if another_item == "yes":
    item_2 = input("Enter the name of item you want to order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")
print(f"The total amount of items to pay is Rs.{order_total}")