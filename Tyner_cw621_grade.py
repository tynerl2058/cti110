#Tyner_cw621_grade
#grade
#Layton Tyner
#21 Jun 2018

#use the if/else structure to determine a letter grade

#Get input from the user

grade = int(input("Give the numeric received for homework "))

if grade >= 90 and grade < 101:
    print("You received an A!")
    print("Your numeric grade of",grade,"is an A!")
#could also use > 89
elif grade >= 80 and grade < 90:
    print ("You received a B.")
    print("Your numeric grade of",grade,"is an B.")
elif grade >= 70 and grade < 80:
    print ("You received a C.")
    print("Your numeric grade of",grade,"is an C.")
elif grade >= 60 and grade < 70:
    print ("You received a D.")
    print("Your numeric grade of",grade,"is an D.")
elif grade >= 0 and grade < 60:
    print ("You received a F.")
    print("Your numeric grade of",grade,"is an F. Come see me.")
else:
    print ("Invalid input; try again.")
   

