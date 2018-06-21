#CTI-110
#P3HW2 - Software Sales
#Layton Tyner
#21 Jun 2018

# Given a purchase of a software package at $99 each; determine the total based on the numnber purchased and the aprropriate volume discount given

# Use the if/else structure to determine amount of discount

# Get input from the user

# Declare some variables
# Variable              Data type   Definition
# softwarePurchased     int         number of software packages purchased
# totalSales            int         total sales at $99 each (99 time softwarePurchased) times % discount
# totalSaved            int         total saved with discount(99 time softwarePurchased) times % discounted

# Declared variables and initialized to zero

softwarePurchased = 0.0
totalSales = 0.0

# Get the softwarePurchased
softwarePurchased = int(input("Enter the number of software packages purchased: "))

# Calculate the totalSales
totalSales = 99 * softwarePurchased

# Calculate the totalSaved
#totalSaved = (99 * softwarePurchased) * % discount

if softwarePurchased < 10:
    print("Your total cost for the software packages is $",format(totalSales,',.2f'),"and you received no discount (buy ten get one free).")
elif softwarePurchased >= 10 and softwarePurchased < 20:
    totalSales = (99 * softwarePurchased) * 0.9
    totalSaved = (99 * softwarePurchased) * 0.1
    print("Your total cost for the software packages is $",format(totalSales,',.2f'),"and you received a 10% discount of $",format(totalSaved,',.2f'),".")
elif softwarePurchased >= 20 and softwarePurchased < 50:
    totalSales = (99 * softwarePurchased) * 0.8
    totalSaved = (99 * softwarePurchased) * 0.2
    print("Your total cost for the software packages is $",format(totalSales,',.2f')," and you received a 20% discount of $",format(totalSaved,',.2f'),".")
elif softwarePurchased >= 50 and softwarePurchased < 100:
    totalSales = (99 * softwarePurchased) * 0.7
    totalSaved = (99 * softwarePurchased) * 0.3
    print("Your total cost for the software packages is $",format(totalSales,',.2f')," and you received a 30% discount of $",format(totalSaved,',.2f'),".")
else:
    totalSales = (99 * softwarePurchased) * 0.6
    totalSaved = (99 * softwarePurchased) * 0.4
    print("Your total cost for the software packages is $",format(totalSales,',.2f')," and you received a 40% discount of $",format(totalSaved,',.2f'),".")
