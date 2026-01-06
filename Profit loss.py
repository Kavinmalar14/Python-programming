costprice = float(input("Please enter the cost price: "))
saleprice = float(input("Please enter the sale price: "))

if(saleprice > costprice):
    profit = saleprice - costprice
    print("The profit is :", profit)
else:
    print("Sorry Batman no profit")