from consolemenu import *
from consolemenu.items import *
from prettytable import PrettyTable
import time


class Inventory:
    mydict = {}
    mylist = []

    def __init__(self, sku, name, ogq, cquantity, pcost, saleprice, tsales):
        self.sku = sku
        self.name = name
        self.ogq = ogq
        self.cquantity = cquantity
        self.pcost = pcost
        self.saleprice = saleprice
        self.tsales = tsales
        Inventory.mydict[sku] = [name, ogq, cquantity, pcost, saleprice, tsales]

    @staticmethod
    def delete():
        Inventory.formatedtable()
        a = int(input("Enter the part number that you would like to remove. "))
        Inventory.mydict.pop(a)
        input(str(a) + " successfully removed from inventory. Press enter to return back to menu. ")
        Inventory.mylist.append(str(a) + " removed from inventory.")
        if a not in Inventory.mydict:
            input("Part does not exist. Press enter to try again. ")

    @staticmethod
    def view():
        Inventory.formatedtable()
        input("Press Enter to return back to menu. ")

    @staticmethod
    def save():
        with open("inventory.txt", "a") as myfilesave:
            for number in Inventory.mydict.keys():
                mylongstring = str(number) + ': ' + Inventory.mydict.get(number)[
                    0] + '. The original quantity was: ' + str(
                    Inventory.mydict.get(number)[1]) + ". The current quantity is: " + str(
                    Inventory.mydict.get(number)[2]) + \
                               '. The production cost was: ' + str(
                    Inventory.mydict.get(number)[3]) + ". The sales price is: " \
                               + str(Inventory.mydict.get(number)[4]) + '. The sales affiliated with this item are: ' + \
                               str(Inventory.mydict.get(number)[5])
                myfilesave.write(mylongstring)
                myfilesave.write('\n')
        Inventory.mylist.append("Data saved to file.")
        input("Data saved! Press enter to return to menu. ")

    @staticmethod
    def enter():
        while True:
            try:
                l = int(input("Please enter in the stock keeping unit of the item:  "))
                break
            except ValueError:
                input("Input a valid number. Press anything to continue. ")
        m = input("Please enter in the name of the item: ")
        while True:
            try:
                n = int(input("Please enter the original quantity of the item: "))
                if n < 1:
                    input("The quantity must be greater than 0. Press enter to retry. ")
                else:
                    break
            except ValueError:
                input("Input a valid number. Press anything to continue. ")
        while True:
            try:
                o = int(input("Please enter the current quantity. "))
                if o < 1:
                    input("The quantity must be greater than 0. Press enter to retry. ")
                else:
                    break
            except ValueError:
                input("Input a valid number. Press anything to continue. ")
        while True:
            try:
                p = float(input("Please enter in the production cost of the item: "))
                if p < 0:
                    input("The production cost must be greater than 0. Press anything to retry. ")
                else:
                    p = '${:,.2f}'.format(p)
                    break
            except ValueError:
                input("Input a number!, Press enter to retry. ")
        while True:
            try:
                q = float(input("Please enter in the sale price of the item:  "))
                if q < 0:
                    input("The sales price must be greater than 0. Press anything to retry. ")
                else:
                    q = '${:,.2f}'.format(q)
                    break
            except ValueError:
                input("Input a valid number. Press anything to continue. ")
        while True:
            try:
                r = n - o
                print("This item has been sold the following number of times:")
                if r < 0:
                    print("ERROR: There has been a mistakes. The sales are negative. Please go back and check the "
                          "values you have inputted. They can be changed through the editing function. ")
                    break

                else:
                    print(r)
                    break
            except ValueError:
                input("Input a valid number. Press anything to continue. ")
        f = Inventory(l, m, n, o, p, q, r)
        input("Part Number " + str(l) + " entered/updated into system. Press Enter to return to menu.")
        Inventory.mylist.append(str(l) + " entered/updated into system.")

    @staticmethod
    def edit():
        while True:
            Inventory.formatedtable()
            try:
                a = int(input("Enter the SKU of the item that you wish to edit. "))
                if a in Inventory.mydict:
                    break
                else:
                    print("Item does not exist")
            except ValueError:
                input("The item does not exist in your inventory. Press anything to try again. ")
        key = Inventory.mydict[a]
        while True:
            try:
                b = int(input("What do you want to edit? Please enter 0 for the name, 1 for the original quantity, "
                              "2 for the current quantity, 3 for the Production Cost, 4 for the Sales Price, or 5 for "
                              "the total sales affiliated with the item "))
                if b in [0, 1, 2, 3, 4, 5]:
                    break
                else:
                    print("Please enter in valid input.")
            except ValueError:
                input("Please enter an integer, press enter to continue. ")
        if b == 1:
            c = Inventory.mydict.get(a)[1]
            while True:
                try:
                    d = int(input("Enter in the corrected original quantity for the item: "))
                    if d < 1:
                        input("the quantity must be greater than 0. Press enter to retry. ")
                    else:
                        Inventory.mydict[a] = [key[0], d, key[2], key[3], key[4], key[5]]
                        break
                except ValueError:
                    print("Please enter a valid number")
        elif b == 2:
            while True:
                try:
                    d = float(input("Please enter in the new quantity for the item:  "))
                    if d < 0:
                        input("The quantity must be greater than 0. Press enter to retry. ")
                    else:
                        Inventory.mydict[a] = [key[0], key[1], d, key[3], key[4], key[5]]
                        break
                except ValueError:
                    input("Input a valid number. Press anything to continue. ")
        elif b == 3:
            while True:
                try:
                    d = float(input("Please enter in the new production price. "))
                    if d < 0:
                        input("The price must be greater than 0. Press enter to retry. ")
                    else:
                        d = '${:,.2f}'.format(d)
                        Inventory.mydict[a] = [key[0], key[1], key[2], d, key[4], key[5]]
                        break
                except ValueError:
                    input("Input a number!, Press enter to retry. ")
        elif b == 4:
            while True:
                try:
                    d = float(input("Please enter in the new sales price. "))
                    if d < 0:
                        input("The price must be greater than 0. Press enter to retry. ")
                    else:
                        d = '${:,.2f}'.format(d)
                        Inventory.mydict[a] = [key[0], key[1], key[2], key[3], d, key[5]]
                        break
                except ValueError:
                    input("Input a number!, Press enter to retry. ")
        if b == 5:
            while True:
                try:
                    d = int(input("Enter the number of sales affiliated with the item: "))
                    if d < 1:
                        input("the quantity must be greater than 0. Press enter to retry. ")
                    else:
                        Inventory.mydict[a] = [key[0], key[1], key[2], key[3], key[4], d]
                        break
                except ValueError:
                    print("Please enter a valid number")
        if b == 0:
            d = input("Please enter in the part name. ")
            Inventory.mydict[a] = [d, key[1], key[2], key[3], key[4], key[5]]

    @staticmethod
    def history():
        for i in Inventory.mylist:
            print(i)
        input("Press enter to return back to menu.")

    @staticmethod
    def formatedtable():
        myprettytable = PrettyTable()
        myprettytable.field_names = ['SKU', 'Name', 'Original Quantity', 'Current Quantity', 'Production Cost',
                                     'Sales Price', 'Sales']
        for number in Inventory.mydict.keys():
            inventory = Inventory.mydict.get(number)
            name = inventory[0]
            original_quantity = inventory[1]
            current_quantity = inventory[2]
            production_cost = inventory[3]
            sale_price = inventory[4]
            sales = inventory[5]
            myprettytable.add_row(
                [number, name, original_quantity, current_quantity, production_cost, sale_price, sales])
        print(myprettytable)

    @staticmethod
    def sales():
        Inventory.formatedtable()
        a = int(input("Enter the sku of the item that you wish to buy: "))
        if a in Inventory.mydict:
            val = Inventory.mydict[a]
            Inventory.mydict[a] = [val[0], val[1], val[2], val[3], val[4], val[5]]
            z = str(val[0])
            g = int(val[2])
            val[3] = val[3].replace('$', "")
            val[4] = val[4].replace('$', "")
            j = str(val[4])
            x = int(val[5])
            f = open("receipt.txt", "a")
            f.write("=======================================================================")
            f.write("\n")
            f.write("Receipt: ")
            f.write("\n")
            f.write("=======================================================================")
            f.write("\n")
            oops = int(input("How many of " + z + "'s did you buy?: "))
            if oops < 0:
                input("You cannot buy a negative amount. Press enter to retry")
            h = oops
            new_quan = g - h
            sale_n = x + h
            f.write("Item name: " + z + "\n")
            f.write("Number of " + z + "'s that were bought = " + str(oops) + "\n")
            Inventory.mydict[a] = [val[0], val[1], new_quan, val[3], val[4], sale_n]
            f.write("Cost of " + z + " = $" + j + "\n")
            f.write("-----------------------------------------------------------------------")
            f.write("\n")
            val[4] = val[4].replace('$', "")
            b = float(val[4])
            q = h * b
            final = str(q)
            f.write("The subtotal is $" + final + "\n")
            val[4] = val[4].replace('$', "")
            ummm = float(val[4])
            confused = q * 0.07
            confucius = '${:,.2f}'.format(confused)
            confusion = str(confucius)
            f.write("The total is 7% or in this case: " + confusion + "\n")
            total = float(float(q) + float(confused))
            dtotal = '${:,.2f}'.format(total)
            f.write("The total is " + str(dtotal) + "\n")
            f.write("----------------------------------------------------------------------- \n")

    @staticmethod
    def profit():
        while True:
            Inventory.formatedtable()
            try:
                a = int(input("Enter the sku of the item that you wish to find the profit for: "))
                if a in Inventory.mydict:
                    break
                else:
                    print("Item does not exist")
            except ValueError:
                input("The item does not exist in your inventory. Press anything to try again. ")
        val = Inventory.mydict[a]
        Inventory.mydict[a] = [val[0], val[1], val[2], val[3], val[4], val[5]]
        val[3] = val[3].replace('$', "")
        val[4] = val[4].replace('$', "")
        b = float(val[1])
        d = float(val[3])
        e = float(val[4])
        f = float(val[5])
        bought = b * d
        made = e * f
        total = float(made) - float(bought)
        if total < 0:
            print("You have not made profit off this item. You have lost the following number of dollars: ")
            print(abs(total))
            with open("profit_.txt", "a") as myfilesave:
                myfilesave.write('The sales loss for item number ' + str(a) + ' is: $' + str(abs(total)))
                myfilesave.write("\n")
        if total > 0:
            print("The profit for this item is the following number of dollars:")
            print(total)
            with open("profit_.txt", "a") as myfilesave:
                myfilesave.write('The sales profit for item number ' + str(a) + ' is: $' + str(total))
                myfilesave.write("\n")
        else:
            print("You have not made profit off this item")

    @staticmethod
    def receipt():
        print("Your receipt is loading . . . \n")
        time.sleep(2)
        print("Here is your receipt: ")
        print("\n")
        log = open("receipt.txt", "r")
        print(log.read())

    @staticmethod
    def validate():
        print("Here is your receipt: ")
        print("\n")
        log = open("receipt.txt", "r")
        print(log.read())
        edit = open("receipt.txt", "w")
        um = input("Enter yes to validate or no to clear the receipt   ")
        if um == "yes":
            print("Your purchase has beean successful!")
            edit.truncate(0)
        if um == "no":
            print("Your receipt will now be deleted")
            edit.truncate(0)

menu = ConsoleMenu("Parts Inventory")

Enter = FunctionItem("Add an item to the inventory", Inventory.enter)
Delete = FunctionItem("Remove an item from the inventory", Inventory.delete)
View = FunctionItem("View the inventory", Inventory.view)
Edit = FunctionItem("Edit the inventory", Inventory.edit)
Buying_an_Item = FunctionItem("Buy an Item from the Inventory", Inventory.sales)
Receipt = FunctionItem("See your receipt", Inventory.receipt)
Validate = FunctionItem("Validate your receipt and pay", Inventory.validate)
Profit = FunctionItem("Profit", Inventory.profit)
Report = FunctionItem("View Session Activity Report", Inventory.history)

menu.append_item(Enter)
menu.append_item(Edit)
menu.append_item(Delete)
menu.append_item(View)
menu.append_item(Buying_an_Item)
menu.append_item(Receipt)
menu.append_item(Validate)
menu.append_item(Report)
menu.append_item(Profit)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
