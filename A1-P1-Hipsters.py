#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

#Student Name: Andrew Beaver
#Program Title: Hipster's Local Vinyl Records
#Description:  Assignment 1 Part 2

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Display opening message to the user
    print("Hipter's Local Vinyl Records - Customer Order Details")

    #Prompt user to give the customer's name
    customerName = input("\nEnter the customer's name: ")

    #Prompt user to give kilometers
    totalKM = float(input("Enter the distance in kilometers for delivery: "))

    #prompt user to give the cost of records
    recordCost = float(input("Enter the cost of records purchased: "))

    #Math
    deliveryCost = totalKM * 15
    purchaseCost = recordCost * 1.14
    totalCost = purchaseCost + deliveryCost
    #Display summary with name
    print("\nPurchase summary for",customerName)

    #display Delivery cost
    print("Delivery Cost: ${0:,.2f}".format(deliveryCost))
    #Display purchase cost + cost
    print("Purchase Cost: ${0:,.2f}".format(purchaseCost))
    #Display total
    print("Total Cost   : ${0:,.2f}".format(totalCost))

    # YOUR CODE ENDS HERE

main()