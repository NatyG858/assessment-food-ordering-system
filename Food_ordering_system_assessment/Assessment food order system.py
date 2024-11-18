# Source code of the Food ordering system

# List representing the customer's current order.
# Each element is a food or drink item the customer has selected.
# List representing the available food and drink items in the menu.
# Each element is a string corresponding to an item that can be ordered.
# Each index in the `prices` list directly corresponds to an item in the `food` list.
myOrder = ["Pizza", "Cola", "Pasta", "Soup", "Cake", "Coffee", "Tea", "Black Tea", "Milk"]
food = ["Burger", "Fries", "Pizza", "Apple Pie", "Cake", "Coca-Cola", "Coffee", "Tea", "Ice Cream"]
prices = [5, 2, 15, 3, 4, 3, 1, 1, 4]

# List to store the names, costs of food items added to the current order.
myorderFood = []
myorderCost = []
# List to temporarily hold new items or modifications made to the order.
newOrder = []
counter = 0
total = 0
#List to store search results or specific items during the search process.
searchOrder = []

print("""
============================================
|//////////////////////////////////////////|
|==========================================|
|Welcome to QuickBite Food Ordering System!|
|==========================================|
|//////////////////////////////////////////|
============================================
              Main Menu 
============================================
       Enter  : Add order
       Enter  : View my order 
       Enter  : Delete my order
       Enter  : Update my order
       Enter  : Exit
===========================================
		""")

#A loop to continuously prompt the customer for their choice until they decide to exit.
newOption = True #A boolean variable to control the loop for presenting options to the customer.
while newOption:
    customerChoice = input("Please enter an option: ")
    if customerChoice == "add order":
        print("""
===========================================
               Food Menu
===========================================
Burger - £5 | Apple Pie -£3 | Coffee -£1
Fries  - £2 | Cake      -£4 | Tea -£1
Pizza  - £15| Ice Cream -£4 | Coca-Cola -£4
=========================================== 
             """)

        # sub-process Add order
        # A boolean variable to control the loop for adding items to the order.
        # As long as `nextOrder` is `True`, the program will continue prompting the customer to enter item names.
        nextOrder = True
        nextOrder = True
        while nextOrder == True:
            foodOrder = input("Enter Item name:")
            if foodOrder == "Burger":
                myorderFood.append(food[0])
                myorderCost.append(prices[0])
                counter = counter + 1
                total = total + (prices[0])

            elif foodOrder == "Fries":
                myorderFood.append(food[1])
                myorderCost.append(prices[1])
                counter = counter + 1
                total = total + (prices[1])

            elif foodOrder == "Pizza":
                myorderFood.append(food[2])
                myorderCost.append(prices[2])
                counter = counter + 1
                total = total + (prices[2])

            elif foodOrder == "Apple Pie":
                myorderFood.append(food[3])
                myorderCost.append(prices[3])
                counter = counter + 1
                total = total + (prices[3])

            elif foodOrder == "Cake":
                myorderFood.append(food[4])
                myorderCost.append(prices[4])
                counter = counter + 1
                total = total + (prices[4])

            elif foodOrder == "Coca-Cola":
                myorderFood.append(food[5])
                myorderCost.append(prices[5])
                counter = counter + 1
                total = total + (prices[5])

            elif foodOrder == "Coffee":
                myorderFood.append(food[6])
                myorderCost.append(prices[6])
                counter = counter + 1
                total = total + (prices[6])

            elif foodOrder == "Tea":
                myorderFood.append(food[7])
                myorderCost.append(prices[7])
                counter = counter + 1
                total = total + (prices[7])

            elif foodOrder == "Ice Cream":
                myorderFood.append(food[8])
                myorderCost.append(prices[8])
                counter = counter + 1
                total = total + (prices[8])

            else:
                print("Not on menu")# Inform the customer that the entered item is not available in the menu.
            # Prompt the customer to decide if they want to add more items to their order.
            finished = input("Do you like add more? Y/N")
            if finished == "Y":
                nextOrder = True # If the customer wants to add more, keep the loop running.
            else:
                nextOrder = False #If the customer does not want to add more, exit the loop.

        i = 0
        print("ORDER DESCRIPTION")
        print("=======================================")
        print("             RECEIPT                   ")
        print("========================================")
        while i < counter:# It's a loop through all the items in the customer ordering.
            print("Item:" + (myorderFood[i]))
            print("Price:£" + str(myorderCost[i]))
            i = i + 1 # helps to move to the next item in the lists.
        print("========================================")
        print("TOTAL AMOUNT £" + str(total))# Set total amount
        print("========================================")
        print("""
===================================       
        Payment options
===================================       
    Enter 1: Pay by card
    Enter 2: Pay by Cach
===================================    
        """) # Ask the customer for their preferred payment option.
        paymentOption = input("Pay by card? Y/N")
        if paymentOption == "Y":# Check the customer's payment choice.
            print("Payment Instructions")
        else:
            print("Payment by cache upon receipt of the order")
        print("Thank you for your order")
        #Ask if the customer wants to perform another action or finish their interaction
        finished = input("Do you want to choose another option? Y/N")

    # sub-process View my order
    # Check if the customer chose the option to view their order.
    # A loop to handle the customer's actions.
    # Prompt the customer to select a sub-option from the view order menu.
    # If the customer chooses to view all items in their order
    # It will print the full list of items
    if customerChoice == "view my order":
        print("""
    ============================================
                  View order options
    ============================================
           Enter  : View all Items
           Enter  : Search Item     
    ===========================================
            """)
        newOrder = True
        while newOrder == True:
            customerChoice = input("Select an option:")
            if customerChoice == "View all Items":
                print(myOrder)
            elif customerChoice == "Search Item":
                searchOrder = input("Enter Order Name To Search:")
                if (searchOrder in myOrder):
                    print(f"\n=> Record Found Of Order {searchOrder}")
                else:
                    print(f"\n=> No Record Found of This Item: {searchOrder}")  # Error Message

            finished = input("Do you want to choose another option? Yes/No")
            if finished == "Yes":  # Prevents abrupt exits.
                newOption = True
            else:
                newOption = False
                break # Helps to stop the loop
        #finished = input("Do you want to choose another option? Yes/No")
        #if finished == "Yes":  # Prevents abrupt exits.
            #newOption = True
        #else:
            #newOption = False
    # sub-process Delete my order
    # It will display the current list of items in the order to the customer.
    # Prompt the customer to enter the name of the item they wish to remove.
    # Check if the entered item exists in the myOrder list.
    # It will remove the specified item from the myOrder list.
    # Prompt the customer to confirm delete item.
    # It will show that the order has been confirmed and successfully deleted.
    # If the item is not found, It will display an error message
    elif customerChoice == "delete my order":
        print(myOrder)
        deleteOrder = input("Enter Item Name To Remove: ")
        if (deleteOrder in myOrder):
            myOrder.remove(deleteOrder)
            confirmDelete = input(f"\n=>Confirm remove {deleteOrder}? Yes/No\n")
            if confirmDelete == "Yes":
                print("Order confirmed")
                print(f"\n=> Item {deleteOrder} Successfully Deleted \n")
                for order in myOrder:
                    print("=> {}".format(order))
            else:
                print(f"\n=> No Record Found of This Item: {deleteOrder}\n")  # Error Message
                finished = input("Do you want to choose another option? Yes/No")
            if finished == "Yes":  # Prevents abrupt exits.
                newOption = True
            else:
                newOption = False

    # sub-process Update my order
    # it will display the current list of items in the customer's order.
    # Prompt the customer to enter a new item.
    # Ask the customer to confirm their decision to update the order
    # If the customer confirms the update it will be set order update.
    # It will display the updated order list.
    # If the customer wants to stop, set newOption to False.
    # Shows confirmation message
    elif customerChoice == "update my order":
        print("""
=======================================
          Order Details
=======================================
""")
        print(myOrder)
        myOrder.append(input("Enter new item:"))
        confirmUpdate = input("Confirm to update order? Yes/No")
        if confirmUpdate == "Yes":
            orderUpdate = True
            print(" Order Successfully Updated")

            for food in myOrder:
                print(f"===>{food}")
        else:
            orderUpdate = False
            print(" Order is not Updated")
        finished = input("Do you want to choose another option? Yes/No")
        if finished == "Yes":
            newOption = True
        else:
            newOption = False

    # 5. Exit
    # Handle the "Exit" option chosen by the customer
    # If the customer confirms they want to exit
    # It will display the main menu  to allow the customer to perform other actions.
    elif customerChoice == "exit":
        endOption = input("Exit: Yes/No")
        if endOption == "Yes":
            print("Thank you for using the QuikBite Food ordering System")
            break # Helps to stop the loop
        else:
            print("""
============================================
              Main Menu 
============================================
       Enter : Add order
       Enter : View my order 
       Enter : Delete my order
       Enter : Update my order
       Enter : Exit
===========================================
		""")
    finished = input("Back Main Menu? No/Yes")
    if finished == "Yes"   :#Prevents abrupt exits.
        newOption = True
    else:
        newOption = False
        break # Helps to stop the loop