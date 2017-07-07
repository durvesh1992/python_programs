#Shopping Basket

shopping_basket = {}

print "Shopping Basket Options: \n" \
      "1: Add Items \n" \
      "2: Remove Items \n" \
      "3: View Basket \n" \
      "0: Exit Program \n"

option = int(input("Enter an option: "))
while option != 0:
    if option == 1:
        item = raw_input("Enter an Item: ")
        if item in shopping_basket:
            print "Item already in basket"
            qnty = int(input("Enter Quantity: "))
            shopping_basket[item] += qnty
        else:
            qnty = int(input("Enter Quantity: "))
            shopping_basket[item] = qnty
    elif option == 2:
        item = raw_input("Enter an Item")
        del shopping_basket[item]
    elif option == 3:
         for item in shopping_basket:
             print item,":",shopping_basket[item]
    elif option != 0:
        print "Please enter the correct option "
    option = int(input("Enter an option: "))

print "Shoppnig Basket is closed"
