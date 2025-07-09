# import statements
import datetime
from read import productList
from write import buy_note, sell_note, update_OG_product_file
buyList = []
SellList = []

# buy code
def buy():
    """
    A function that is called to buy products.
    parameters: none
    returns: none
    raises: ValueError
    """
    buyId = 0
    buyQuantity = 0
    vatpersent = 13 #in %
    buyDate = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day)
    buyTime = str(datetime.datetime.now().hour) + "hr:"+ str(datetime.datetime.now().minute) + "min:"+ str(datetime.datetime.now().second)+ "s"
    if not buyList:
        buyName = input("Enter name of Supplier: ")
    else:
        buyName = ""
    try:        # exception handled
        buyId = int(input("Enter the Id of the product: "))
    except ValueError:
        print("Please enter a valid ID!")
        print("-"*150)
        buy()
    if buyId < 0:
        print("Id cannot be in negative")
        buy()
    if 0 < buyId <= len(productList):
        try:
            buyQuantity = int(input("Enter the quantity of the product (Available: "+str(productList[buyId - 1].quantity)+"): "))
        except ValueError:
            print("Please enter a valid number!")
            print("-" * 150)
            buy()
            # check for quantity not being negative
        if buyQuantity < 0:
            print("Quantity cannot be negative!")
            buy()
        else:
            print("-"*150)
            total_without_vat = productList[buyId - 1].costPrice * buyQuantity
            total = total_without_vat * (vatpersent / 100)
            #incresed quantity
            productList[buyId - 1].quantity += buyQuantity
            print("Your total is", total, " including VAT.")
            print(str(buyQuantity) + " unit of " + productList[buyId - 1].productName + " added in inventory.")
            print("-" * 150)
            update_OG_product_file()
            purchaseList = [buyDate, buyTime, buyName, buyId, productList[buyId - 1].productName, productList[buyId - 1].brand, productList[buyId - 1].costPrice, buyQuantity, total]
            buyMore(purchaseList)
    else:
        print("product ID not found!")
        print("-"*150)
        buy()


# code run for buying more
def buyMore(purchase_List):
    """
    A function that asks the user if they want to buy more products.
    parameters: purchase_List
    returns: none
    raises: none
    """
    buyList.append(purchase_List)
    buy_more = input("Want to buy more? [Y/N]: ").lower()
    if buy_more == "y":
        buy()
    elif buy_more == "n":
        print("Thank You for Purchasing")
        print("-" * 150)
        printBill(buyList)
        buy_note(buyList)
        while buyList:
            buyList.pop()
    else:
        print("Invalid input. Please enter Y or N.")
        buyMore(purchase_List)


# code to print bill in console
printBillno = [1]

def printBill(myBill):
    """
    A function that Generates and prints an invoice/bill in console of buy.
    parameters: myBill
    returns: none
    raises: none
    """
    print("=" * 49)
    print(" " * 10 + "WeCare: Grow Naturally")
    print("=" * 49)

    print("Bill no:\t" + str(printBillno[0]))
    print("Supplier:\t" + buyList[0][2])
    print("Date:\t" + buyList[0][0])
    print("Time:\t" + buyList[0][1])

    print("-" * 86)
    print("S.N.  ID       Name                             Brand              Quantity   Price     Total")
    print("-" * 86)

    Gtotal = 0
    count = 1

    for e in buyList:
        print(
            str(count) + " " * (6 - len(str(count))) +
            str(e[3]) + " " * (9 - len(str(e[3]))) +
            e[4] + " " * (30 - len(e[4])) +
            e[5] + " " * (23 - len(e[5])) +
            " " * (10 - len(str(e[7]))) + str(e[7]) +
            " " * (9 - len(str(e[6]))) + str(e[6]) +
            " " * (9 - len(str(round(e[8], 2)))) + str(round(e[8], 2))
        )
        Gtotal += e[8]
        count += 1

    print("-" * 86)
    print(
        "Total Amount (including Vat):" +
        " " * (86 - len("Total Amount (including Vat):") - len(str(round(Gtotal, 2)))) +
        str(round(Gtotal, 2))
    )
    print("-" * 86)
    print(" " * 20 + "Thank you for doing Business With Us!")
    print("=" * 49)
    printBillno[0] = printBillno[0] + 1


# selling code
def sell():
    """
    A function that is called to sell products.
    parameters: none
    returns: none
    raises: ValueError
    """
    sellDate = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day)
    sellTime = str(datetime.datetime.now().hour) + "hr:"+ str(datetime.datetime.now().minute) + "min:"+ str(datetime.datetime.now().second) +"s"
    if not SellList:
        sellName = input("Enter name of Supplier: ")
    else:
        sellName = ""
    sellId = 0
    sellQuantity = 0
    totalCharge = 0
    try:
        sellId = int(input("Enter the Id of the product: "))
    except ValueError:
        print("Please enter a valid number!")
        print("-"*150)
        sell()
    if sellId < 0:
        print("Id cannot be in negative")
    if 0 < sellId <= len(productList):
        try:
            sellQuantity = int(input("Enter the quantity of the product (Available: "+str(productList[sellId - 1].quantity)+"): "))
        except ValueError:
            print("Please enter a valid number!")
            print("-" * 60)
            sell()
        if sellQuantity < 0:
            print("Quantity cannot be negative!")
            print("-" * 60)
            sell()
        else:
            extraQuantity = sellQuantity // 3
            finalQuantity = sellQuantity + extraQuantity
            sellPrice = productList[sellId - 1].costPrice * 2
            totalCharge = sellPrice * sellQuantity
            if finalQuantity <= productList[sellId - 1].quantity:
                productList[sellId - 1].quantity -= finalQuantity
                print("-"*150)
                print("Sold " + str(sellQuantity)+ " + " + str(extraQuantity) + " free units of " + productList[sellId - 1].productName + " to " +sellName+" successfully.")
                print("Your total is Rs "+str(totalCharge)+".")
                saleList = [sellDate, sellTime, sellName, sellId, productList[sellId - 1].productName, productList[sellId - 1].brand, sellPrice, sellQuantity, extraQuantity, totalCharge]
                update_OG_product_file()
                sellMore(saleList)
            elif sellQuantity > productList[sellId - 1].quantity:
                print("Not enough quantity in stock")
                print("-" * 150)
                sell()
            else:
                finalPayQuantity = sellQuantity - extraQuantity
                totalCharge = finalPayQuantity * sellPrice

                productList[sellId - 1].quantity -= sellQuantity
                print("-" * 150)
                print("Sold " + str(finalPayQuantity) + " + " + str(extraQuantity) + " free units of " + productList[
                        sellId - 1].productName + " to " + sellName + " successfully.")
                print("Your total is Rs " + str(totalCharge) + ".")
                update_OG_product_file()
                saleList = [sellDate, sellTime, sellName, sellId, productList[sellId-1].productName,productList[sellId-1].brand, sellPrice, sellQuantity, extraQuantity,totalCharge]
                sellMore(saleList)
    else:
        print("product ID not found!")
        print("-"*150)
        sell()

# code to sellMore items
def sellMore(saleList):
    """
    A function that asks the user if they want to sell more products.
    parameters: saleList
    returns: none
    raises: none
    """
    SellList.append(saleList)
    sellMoreChoice = input("Do you want to sell more products?[Y/N]: ").lower()
    if sellMoreChoice == "y":
        print("-" * 150)
        sell()
    elif sellMoreChoice == "n":
        print("Thank You for Selling")
        print("-" * 150)
        printSellBill(SellList)
        sell_note(SellList)
        while SellList:
            SellList.pop()
    else:
        print("Invalid input. Please enter Y or N.")
        sellMore(saleList)


sell_no = [1]
# print a invoice in console
def printSellBill(sellList):
    """
    A function that Generates and prints a bill in console.
    parameters: sellList
    returns: none
    raises: none
    """
    print("=" * 49)
    print(" " * 10 + "WeCare: Grow Naturally")
    print("=" * 49)

    print("Bill no:\t" + str(sell_no[0]))
    print("Customer:\t" + sellList[0][2])
    print("Date:\t" + sellList[0][0])
    print("Time:\t" + sellList[0][1])

    print("-"*86)
    print("S.N.  ID       Name                             Brand              Quantity   Price     Total")
    print("-" * 86)

    Gtotal = 0
    count = 1
    freeItems = 0
    for e in sellList:
        print(
            str(count) + " " * (6 - len(str(count))) +
            str(e[3]) + " " * (9 - len(str(e[3]))) +
            e[4] + " " * (30 - len(e[4])) +
            e[5] + " " * (23 - len(e[5])) +
            " " * (10 - len(str(e[7]))) + str(e[7]) +
            " " * (9 - len(str(e[6]))) + str(e[6]) +
            " " * (9 - len(str(round(e[9], 2)))) + str(round(e[9], 2))
        )
        Gtotal += e[9]
        freeItems += e[8]
        count += 1

    print("-" * 86)
    print("Total Amount:" + " " * (86 - len("Total Amount:") - len(str(round(Gtotal, 2)))) + str(round(Gtotal, 2)))
    print("Free Items:" + " " * (86 - len("Free Items:") - len(str(freeItems))) + str(freeItems))
    print("-" *86)
    print(" " * 20 + "Thank you and visit us again...")
    print("=" * 49)
    sell_no[0] = sell_no[0] + 1
