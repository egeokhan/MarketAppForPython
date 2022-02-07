productnameList = []
productpriceList = []
allproductList = []
allpriceList = []
allbarcodeList = []
ffile = open("Products.txt","r")
for line in ffile:
    listline = line.rstrip("\n").split(";")
    allbarcodeList.append(listline[0])
    allproductList.append(listline[1])
    allpriceList.append(listline[2])
while True:
    print("--------------------------------")
    menu = int(input("Press 1 for search a product\nPress 2 to see the basket\nPress 3 for products\nPress 4 for exit\nPress: "))
    if menu == 1:
        file = open("Products.txt","r")
        find = False
        print("--------------------------------")
        barcode = input("Product Barcode: ")
        for line in file:
            listline = line.rstrip("\n").split(";")
            if barcode == listline[0]:
                productname = listline[1]
                productprice = listline[2]
                find = True
        if find == True:
            print("--------------------------------")
            print(f"Name: {productname}\nPrice: {productprice}$")
            print("--------------------------------")
            addtobasket = input("Do you want to add to cart? Y/N: ")
            if addtobasket.upper() == "Y":
                productnameList.append(productname)
                productpriceList.append(productprice)
            else:
                continue
        else:
            print("--------------------------------")
            print("Product not found...")
        file.close()
    elif menu == 2:
        i = 0
        print("--------------------------------")
        while i < len(productnameList):
            productline = f"Product Name: {productnameList[i]} --- Price: {productpriceList[i]}$"
            print(productline)
            i+=1
        result = 0
        for price in productpriceList:
            result += int(price)
        print(f"Result: {result}$")
    elif menu == 3:
        j = 0
        print("--------------------------------")
        while j < len(allproductList):
            menuline = f"Barcode: {allbarcodeList[j]} --- Name: {allproductList[j]} --- Price: {allpriceList[j]}$"
            print(menuline) 
            j+=1
    elif menu == 4:
        print("GoodBye!")
        break
