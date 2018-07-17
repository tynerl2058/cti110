#CTI-110
#P5T1 - Kilometer Converter
#Layton Tyner
#10 Ju1 2018

# Declare some variables
# Variable   	Data type   Definition
# distKm        float       distance in Kilometers (Km)
# convKtoM  	float       conversion factor equal to 0.6214
# distToMiles  	float       distKm times convKtoM

# Declared variables and initialized to zero

distKm = 0.0
convKtoM = 0.6214
distToMiles = 0.0

def main():
    displayComments()
    distKm = getDistKm()
    convKtoM = 0.6214
    distToMiles = calculateDistToMiles(distKm,convKtoM)
    displayDistToMiles(distToMiles)

def displayComments():
    print("This program will convert distance in kilometers to miles.")
    print(" ")

def getDistKm():
    distKm = float(input("What is the distance in kilometers? "))
    return distKm

def calculateDistToMiles(d,c):
    return d * c

def displayDistToMiles(distToMiles):
    print(" ")
    print("The conversion from kilometers is",format(distToMiles,',.2f'),"miles.")

main()
