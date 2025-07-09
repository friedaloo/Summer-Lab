'''A Python application that that can read the data from a file then load it in the system so
that user can operate through the products like buying and selling and track products
records to boost their sales.'''

'''
Used concept:- 
OOP (Class and Objects)
collections (List, Dictionary)
primitive datatype (int, boolean, float, String)
Exception handling
file Handling
Conditional and looping statements
functions
'''

from Operation import buy, sell
from read import productList

# getting choice from user
def inputChoice():
    """
    A function that takes user input and displays the appropriate menu.
    parameters: None
    returns: None
    raises: None
    """

    print("What do you want to do!")
    print("1 -> Display products available in store.")
    print("2 -> Restock products.")
    print("3 -> Sell to Customers")
    print("4 -> Exit form System.")
    print("-"*150)
    choice = input("Enter choice: ")

    if choice == '1':
        for element in productList:
            element.productDisplay()
        inputChoice()

    elif choice == '2':
        print("-" * 150)
        print("ID\tName\t\t\t\tBrand\t\tQuantity\tCost(Rs)\tSelling(Rs)\tCountry")
        print("-" * 150)
        for element in productList:
            element.buy_sell_display()
        print("-" * 150)
        buy()
        inputChoice()
    elif choice == '3':
        print("-" * 150)
        print("ID\tName\t\t\t\tBrand\t\tQuantity\tCost(Rs)\tSelling(Rs)\tCountry")
        print("-" * 150)
        for element in productList:
            element.buy_sell_display()
        print("-" * 150)
        sell()
        inputChoice()
    elif choice == '4':
        print("Thank you for visiting...")
        print("-" * 150)
        #exit()

    else:
        print("Enter valid choice!")
        inputChoice()

def load():
    """
    A function that loads whole application.
    parameters: None
    returns: None
    raises: None
    """
    print("\n" + "*" * 60)
    print(" " * 15 + "WeCare: Grow Naturally")
    print("*" * 60 + "\n")
    inputChoice()

#run program
load()
