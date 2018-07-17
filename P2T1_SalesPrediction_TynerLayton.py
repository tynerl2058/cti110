#CTI-110
#P2T1 - Sales Prediction
#Layton Tyner
#14 Jun 2018
#

# Declare some variables
# Variable  	Data type  Definition
# totalSales    float      total sales by the company in $
# profitMargin  float      profit margin determined at 23% (0.23)
# annualProfit	float      totalSales times profitMargin equals annualProfit in $

# Declared variables and initializd to zero

totalSales = 0.0
profitMargin = 0.0
annualProfit = 0.0

# get the totalSales
totalSales = float(input("Enter the total sales: "))

# get the profitMargin 24%
profitMargin = 0.23

# totalSales times profitMargin will be assigned to annualProfit
annualProfit = totalSales * profitMargin

print("Your annual profit is $",annualProfit)
