# Inventory Capstone project
# Resubmission:
#I've now printed the product is for sale for the high stock item
#I've written the code to write the restock to the txt file

# Creating Shoe class
class Shoe():
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
        self.value = quantity*cost #have included value here as a class varibale

# Creating get_cost methods
    def get_cost(self):
        return self.cost


# Creating get_quanty method
    def get_quanty(self):
        return self.quantity


# Creating set_qunatity method
    def set_quantity(self,quantity):
        self.quantity += quantity


# creating get_value method
    def get_value(self):
        return self.value


 # Creating the string method   
    def __str__(self) -> str: 
        return f"\nCountry: {self.country}\n"\
            f"Code: {self.code}\n"\
            f"product: {self.product}\n"\
            f"Cost: {self.cost}\n"\
            f"Quantity: {self.quantity}\n" \
            f"Value: {self.value}"


# Creating Read shoes data function
def read_shoes_data():
    try:
        shoe_list_val = []
        with open("inventory.txt", "r") as f:
            file_contents = f.readlines()
            for line in file_contents[1:]:
                line_list = line.strip("\n").split(",")
                shoe_object = Shoe(line_list[0],line_list[1],line_list[2],int(line_list[3]), int(line_list[4]))
                shoe_list_val.append(shoe_object)
        return shoe_list_val
# Creating an exception for if file not found
    except FileNotFoundError:
        print("This file does not exist")


# Creating capture function
def capture_shoes():
    country = input("Shoe country: ")
    code = input("Shoe code: ")
    shoe_product = input("Name of product: ")
    shoe_cost = int(input("Shoe cost: "))
    shoe_quantity = int(input("Shoe quantity: "))
    shoe_object = Shoe(country , code, shoe_product, shoe_cost, shoe_quantity)
    shoe_list.append(shoe_object)
    print("Thank you, your item has been captured")


# Creating view all function
def view_all():
    for i in shoe_list:
        print(i)

        
# Creating restock function
def re_stock():
    low_stock = shoe_list[0]
    # Creating for loop to determine object with lowest stock
    for i in shoe_list:
        if i.get_quanty() <= low_stock.get_quanty(): 
            low_stock = i 
    print(low_stock)
    # Allowing user to restock and printing new stock
    new_stock = int(input("How much additional stock would you like to add: "))
    low_stock.set_quantity(new_stock)
    print(f"The new stock value for this item is {low_stock.get_quanty()}")
    #Writing new stock to the txt file
    with open("inventory.txt",'w') as f:
           f.write("Country,Code,Product,Cost,Quantity")
           for i in shoe_list:
            f.write(f"\n{i.country},{i.code},{i.product},{i.cost}, {i.quantity}\n")

# Creating search function
def search_shoe():
    requested_code = input("Please enter the code of the shoe you are loooking for: ")
    for i in shoe_list:
        if requested_code == i.code:
            print(i)

# Just putting this here as I know its a requirement for the task but I've included this as a class variable above
# def value_per_item():
#     for i in shoe_list:
#         item_value = i.cost * i.quantity
#         print(item_value)

# Creating highest quantity function
def highest_qty():
    print(shoe_list)
    highest_stock = shoe_list[0]
    for i in shoe_list:
        if i.get_quanty() >= highest_stock.get_quanty():
            highest_stock = i
    print("This shoe is for sale:\n" + highest_stock)

# Creating shoe_list and calling read_shoe_data so rest of code can run
shoe_list = read_shoes_data()


# Creating menu
while True:
    menu = input('''
    Please select an option:       Selection:
    Capture new shoe data:           1
    View details of all shoes:       2
    View shoe with lowest quantity:  3
    View shoe with highest quantity: 4
    Search for a specific shoe:      5
    Exit                             e
    
    Selection: ''')

# Setting up conditional statments to match menu selection and call the relevant function
    if menu == "1":
        capture_shoes()

    elif menu == "2":
        view_all()

    elif menu == "3":
        re_stock()

    elif menu == "4":
        highest_qty()

    elif menu == "5":
        search_shoe()
#Exist option to avoid infinite loop
    elif menu == "e":
        print("Goodbye!")
        exit()

# Else statement if wrong selection is made
    else: 
        print("You've entered an invalid value, please try again")

