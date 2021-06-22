grocery_list = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}
shapes = {"triangle":3, "square":4, "rectangle":4, "pentagon":5, "hexagon":6}
triangle_sides = shapes ["triangle"]
print(shapes ["triangle"])
print(triangle_sides)

#accessing the grocery_list dictionary
chicken_price = grocery_list ["chicken"]
beef_price = grocery_list ["beef"]
cheese_price = grocery_list ["cheese"]
milk_price = grocery_list ["milk"]

grocery_list ["chicken"] = 1.50
grocery_list ["beef"] -= 0.09

print(grocery_list ["chicken"])
print(grocery_list ["beef"])

shoe_inv = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
shoe_inv ["SB Dunk"] -= 2
shoe_inv ["Yeezy"] += 1
#shoe_inv += 7
#shoe_inv -= 3
print (shoe_inv)

shoe_inv ["Air Force"] = 15
print (shoe_inv)

#function 2
def restock (shoe_name, multiplier):
    newInv = shoe_inv[shoe_name] * multiplier
    shoe_inv[shoe_name] = newInv
    return shoe_inv

print (restock("Yeezy", 3))


#functions
def total (p1,p2):
    price = grocery_list [p1] + grocery_list [p2]
    return price

print (total("chicken", "beef"))


    
