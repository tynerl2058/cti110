#CTI-110
#P4HW1 - Distance Traveled
#Layton Tyner
#1 Ju1 2018

# Declare some variables
# Variable   	Data type  Definition
# speed         float      speed of vehicle
# hour   	float      time in hours
# distance  	float      speed times time

# Declared variables and initialized to zero

speed = 0.0
hour = 0
distance = 0.0

def main():
    displayComments()
    speed = getSpeed()
    hour = getHoursTraveled()
    distance = calculateDistance(speed,hour)
    displayDistance(speed,hour)

def displayComments():
    print("This program will calculate distance traveled hour by hour.")
    print(" ")

def getSpeed():
    speed = float(input("What is the speed of the vehicle in mph? "))
    return speed

def getHoursTraveled():
    hour = int(input("How many hours has the vehicle traveled? "))
    return hour

ftitle = "Hours"
stitle = "Distance Traveled"

def calculateDistance(s,h):
    return s * h

def displayDistance(s,h):
    print(" ")
    print(ftitle.ljust(10)+ stitle.ljust(10))
    print("-" * 30)
# run for loop to get the distance traveled for each hour
    for i in range(1,h+1):
        print(str(i).ljust(10) + str(s*i).ljust(6)+"miles")



main()
