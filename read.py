# class constructed name products
class Products:
    # constructor
    def __init__(self, productId, productName, brand, quantity, costPrice, country):
        """
        A constructor that initializes the product object.
        parameters: productId, productName, brand, quantity, costPrice, country
        returns: none
        raises: none
        """
        # variables
        self.productId = productId
        self.productName = productName
        self.brand = brand
        self.quantity = quantity
        self.costPrice = costPrice
        self.country = country

    # Function
    def productDisplay(self):
        """
        A function that displays the product details.
        parameters: none
        returns: none
        raises: none
        """
        name = self.productName
        brand = self.brand
        quantity = str(self.quantity)
        cost = "Rs " + str(self.costPrice)
        selling = "Rs " + str(self.costPrice * 2)
        country = self.country

        print("Product " + str(self.productId) + ":")
        print("-" * 15)
        print("  Name\t\t\t: " + name)
        print("  Brand\t\t\t: " + brand)
        print("  Quantity\t\t: " + quantity)
        print("  Cost Price (Rs)\t\t: " + cost)
        print("  Selling Price (Rs)\t\t: " + selling)
        print("  Country\t\t\t: " + country)
        print("-" * 150)

    def buy_sell_display(self):
        """
        A function that displays the product details in tabular format.
        parameters: none
        returns: none
        raises: none
        """
        name = self.productName + " " * (45 - len(self.productName))
        brand = self.brand + " " * (15 - len(self.brand))
        quantity = str(self.quantity)
        cost = "Rs " + str(self.costPrice)
        selling = "Rs " + str(self.costPrice * 2)
        country = self.country
        print(
            str(self.productId) + "\t" + name + "\t" + brand + "\t" + quantity + "\t" + cost + "\t" + selling + "\t\t" + country)


# Initialize Dictionary
data = {}
productCount = 0  # keeping count of the product
lines = []

# Read file
try:
    with open("product.txt", 'r') as file:
        lines = file.read().split("\n")
    file.close()
except FileNotFoundError:
    print("File not found.")
    exit()
# Read lines
i = 1
for line in lines:
    if line == "":
        continue
    row = line.split(",")

    row[2] = int(row[2])  # Quantity
    row[3] = int(row[3])  # Cost Price
    data[i] = row  # storing row list in dictionary as value with 'i' as key
    productCount += 1
    i += 1

# Create and store product objects
productList = []
i = 1
while i <= productCount:
    info = data[i]
    productObj = Products(i, info[0], info[1], info[2], info[3], info[4])  # creating object
    productList.append(productObj)  # Storing object in productList
    i += 1