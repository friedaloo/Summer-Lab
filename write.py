# product buy invoice code
from read import productList

bill_no = [1]
def buy_note(buyList):
    """
    A function that takes some parameters and generates a buy invoice in a txt file.
    parameters: buyList
    returns: none
    raises: none
    """
    fileName = "buy_note "+str(bill_no[0])+".txt"
    with open(fileName, "w") as file:
        file.write("=" * 78 + "\n")
        file.write("\t\t\t\tWeCare: Grow Naturally\n")
        file.write("=" * 78 + "\n")

        file.write("    Bill no:\t" + str(bill_no[0]) + "\n")
        file.write("    Supplier:\t" + buyList[0][2] + "\n")
        file.write("    Date:\t" + buyList[0][0] + "\n")
        file.write("    Time:\t" + buyList[0][1] + "\n")

        file.write("-" * 78 + "\n")
        file.write("S.N.  ID        Name                Brand        Quantity   Price    Total\n")
        file.write("-" * 78 + "\n")

        Gtotal = 0
        count = 1

        for e in buyList:
            file.write(" " + str(count) + " " * (6 - len(str(count))) +
                        str(e[3]) + " " * (9 - len(str(e[3]))) +
                        e[4] + " " * (20 - len(e[4])) +
                        e[5] + " " * (15 - len(e[5])) +
                        str(e[7]) + " " * (10 - len(str(e[7]))) +
                        str(e[6]) + " " * (8 - len(str(e[6]))) +
                        str(round(e[8], 2)) + "\n")
            Gtotal += e[8]
            count += 1

        file.write("-" * 78 + "\n")
        totalLine = "    Total Amount (including Vat):"
        file.write(totalLine + " " * (75 - len(totalLine) - len(str(round(Gtotal, 2)))) + str(round(Gtotal, 2)) + "\n")
        file.write("-" * 78 + "\n")
        file.write("\t\t\t  Thank you for doing Business With Us!\n")
        file.write("=" * 78 + "\n")
    bill_no[0] = bill_no[0] + 1     # increase bill no by 1

sell_no = [1]
# generate a txt file of invoice
def sell_note(sellList):
    """
    A function that takes some parameters and generates a sell invoice in a txt file.
    parameters: sellList
    returns: none
    raises: none
    """
    fileName = "sell_note "+str(sell_no[0])+".txt"
    with open(fileName, "w") as file:
        file.write("=" * 78 + "\n")
        file.write("\t\t\t\tWeCare: Grow Naturally\n")
        file.write("=" * 78 + "\n")

        file.write("    Bill no:\t" + str(sell_no[0]) + "\n")
        file.write("    Customer:\t" + sellList[0][2] + "\n")
        file.write("    Date:\t" + sellList[0][0] + "\n")
        file.write("    Time:\t" + sellList[0][1] + "\n")

        file.write("-" * 78 + "\n")
        file.write("S.N.  ID        Name                Brand        Quantity   Price    Total\n")
        file.write("-" * 78 + "\n")

        Gtotal = 0
        count = 1
        freeItems = 0

        for e in sellList:
            file.write(" " + str(count) + " " * (6 - len(str(count))) +
                        str(e[3]) + " " * (9 - len(str(e[3]))) +
                        e[4] + " " * (20 - len(e[4])) +
                        e[5] + " " * (15 - len(e[5])) +
                        str(e[7]) + " " * (10 - len(str(e[7]))) +
                        str(e[6]) + " " * (8 - len(str(e[6]))) +
                        str(round(e[8], 2)) + "\n")
            Gtotal += e[9]
            freeItems += e[8]
            count += 1

        file.write("-" * 78 + "\n")
        file.write("    Total Amount:" + " " * (75 - len("    Total Amount:") - len(str(round(Gtotal, 2)))) + str(round(Gtotal, 2)) + "\n")
        file.write("    Free Items:" + " " * (75 - len("    Free Items:") - len(str(freeItems))) + str(freeItems) + "\n")
        file.write("-" * 78 + "\n")
        file.write("\t\t\t  Thank you and visit us again..." + "\n")
        file.write("=" * 78 + "\n")
    sell_no[0] = sell_no[0] + 1

# Code to update Product.txt
def update_OG_product_file():
    """
    updates Original txt file with new product details
    parameters: none
    returns: none
    raises: FileNotFoundError
    """
    try:
        with open("product.txt", "w") as file:
            for product in productList:
                line = product.productName + "," + product.brand + "," + str(product.quantity) + "," + str(
                    product.costPrice) + "," + product.country + "\n"
                file.write(line)
    except FileNotFoundError:
        print("File not found.")
