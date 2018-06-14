#CTI-110
#P2HW2 - Tip Tax Total
#Layton Tyner
#14 Jun 2018
#

# Declare some variables
# Variable   Data type  Definition
# foodCost   float      initial charge for meal
# salesTax   float      7% of meal cost (0.07 * foodCost)
# tipAmount  float      18% gratuity (tip) applied to meal (0.18 * foodcost)
# totalCost  float      food cost with tax & tip (foodCost + salesTax + tipAmount)


# Declared variables and initializd to zero

foodCost = 0.0
salesTax = 0.0
tipAmount = 0.0
totalCost = 0.0

# get the foodCost
foodCost = float(input("Enter the initial charge for meal: "))

# get the salesTax
salesTax = 0.07 * foodCost

# get the tipAmount
tipAmount = 0.18 * foodCost

# foodCost + salesTax + tipAmount will be assigned to totalCost
totalCost = foodCost + salesTax + tipAmount

print("Your total cost of the meal is $",totalCost)
