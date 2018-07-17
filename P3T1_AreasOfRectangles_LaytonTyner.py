
#CTI-110
#P3T1 - Areas of Rectangles
#Layton Tyner
#19 Jun 2018
#

# Declare some variables
# Variable   	Data type  Definition
# lengthRect1   float      length of rectangle 1
# widthRect1   	float      width of rectangle 1
# areaRect1  	float      area of rectangle 1
# lengthRect2   float      length of rectangle 1
# widthRect2   	float      width of rectangle 2
# areaRect2  	float      area of rectangle 2

# Declared variables and initialized to zero

lengthRect1 = 0.0
widthRect1 = 0.0
areaRect1 = 0.0
lengthRect2 = 0.0
widthRect2 = 0.0
areaRect2 = 0.0

# get the length of rectangle 1
lengthRect1 = float(input("Enter the length of rectangle 1: "))

# get the width of rectangle 1
widthRect1 = float(input("Enter the width of rectangle 1: "))

# get the length of rectangle 2
lengthRect2 = float(input("Enter the length of rectangle 2: "))

# get the width of rectangle 2
widthRect2 = float(input("Enter the width of rectangle 2: "))

# Calculate the areas of rectangles
areaRect1 = lengthRect1 * widthRect1
areaRect2 = lengthRect2 * widthRect2

# Determine which rectangle has the greater area
if areaRect1 > areaRect2:
    print ("Rectangle 1 has the greater area.")
elif areaRect2 > areaRect1:
    print ("Rectangle 2 has the greater area.")
else: 
    print ("Both rectangles have the same area.")
