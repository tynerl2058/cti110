#CTI-110
#P5T2 - Feet to Inches
#Layton Tyner
#10 Ju1 2018

# Declare some variables
# Variable   	Data type   Definition
# distFeet      float       distance in Feet (ft)
# convFtoI  	int         conversion factor one foot equals to 12 inches
# distToInches  float       distFeet times convFtoI

# Declared variables and initialized to zero

distFeet = 0.0
convFtoI = 0.6214
distToInches = 0.0

def main():
    displayComments()
    distFeet = getDistFeet()
    convFtoI = 12
    distToInches = calculateDistToInches(distFeet,convFtoI)
    displayDistToInches(distFeet,distToInches)

def displayComments():
    print("This program will convert distance in feet to inches.")
    print(" ")

def getDistFeet():
    distFeet = float(input("What is the distance in feet? "))
    return distFeet

def calculateDistToInches(d,c):
    return d * c

def displayDistToInches(distFeet,distToInches):
    print(" ")
    print("The conversion from ",distFeet,"feet is",format(distToInches,',.2f'),"inches.")

main()
