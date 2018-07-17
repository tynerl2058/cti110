#
#13 Jun 2018
#CTI-110 P5HW1 - Test Average and Grade
#Layton Tyner
#

# Declare some variables
# Variable   	Data type   Definition
# score         int         numeric test score greater than zero
# average       int         average of five numeric test scores
# grade         str         grade based off average test score
# result   	int         the average test score and corresponding letter grade

# Declared variables are initialized to zero
#grade = 0
#total = 0

def main():
# This program takes five test scores and give the average along with the letter grade.
    displayComments()
    average = getScore()
    grade = determineGrade(average)
    displayResult(average,grade)

def displayComments():
    print("This program will give the average and grade for five test scores.")
    print(" ")
    
# get the numeric grades to average
def getScore():
    score1 = int(input("Enter first test score. "))
    score2 = int(input("Enter second test score. "))
    score3 = int(input("Enter third test score. "))
    score4 = int(input("Enter fourth test score. "))
    score5 = int(input("Enter fifth and last test score. "))
    return (score1 + score2 + score3 + score4 + score5)/5
##
##def calcAverage(average):
##    total = 0
##    CalculateAverage = (score + total)/5
##    return average

def determineGrade(average):
    if average >= 90:
        letterGrade = ("A")
    elif average >= 80:
        letterGrade = ("B")
    elif average >= 70:
        letterGrade = ("C")
    elif average >= 60:
        letterGrade = ("D")
    else:
        letterGrade = ("F")
    return letterGrade
    
def displayResult(average,grade):
    print ("")
    print ("The average test score is ",average," which give a letter grade of ",grade,".",sep="")
    
# program start
main()
