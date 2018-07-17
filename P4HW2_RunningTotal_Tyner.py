#CTI-110
#P4HW2 - Running Total
#Layton Tyner
#13 Jun 2018

# Declare some variables
# Variable   	Data type   Definition
# grade         int         numeric grade greater than zero
# total   	int         total of all numeric grades

# Declared variables are initialized to zero
#grade = 0
#total = 0

def main():
# This program takes a series of numbers until a negative one is inputted and then totals the numbers.
    displayComments()
    total = getGrade()
    #total = calculateTotal(grade)
    displayTotal(total)

def displayComments():
    print("This program will total numeric grades.")
    print("To complete sum give a negative number.")
    print(" ")
    
# get the numeric grades to total
def getGrade():
    total = 0
    grade = int(input("Enter non-negative numeric test grade. "))
    while grade >= 0:
        total = grade + total
        grade = int(input("Enter non-negative numeric test grade. "))
    return total

def displayTotal(total):
    print ("")
    print ("Total: ",total)
    
# program start
main()
