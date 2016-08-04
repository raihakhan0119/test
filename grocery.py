print("Welcome to ShopRite!")

groceries = {}

def create_list():
	choice = input("Would you like to add an item? Type yes or no: ")
	if choice == "yes":
		add_item()
	
def add_item():
	item = input("What item would you like to add? ")
	quantity = input("How many " + item + "s would you like to add? ")
	groceries[item] = quantity
	print(groceries)
	

def remove_item():
	item = input("What item would you like to take away?")
	del groceries["item"]
	print(groceries)

def update_item():
	choice = input("What would you like to update?")
	quantity_1 = input("How many of " + choice + " are there now?")
	groceries[choice] = quantity_1
	
create_list()