#CTI-110
#P3LAB2 - Determine Grade
#Layton Tyner
#22 Jun 2018

# Declare some variables
# Variable  Data type  Definition
# score     int      numeric grade received 0-100

# Declared variables and initializd to zero

def main():
# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59

    
score = int(input('Enter grade: '))

if score >= 90:
    print('Your grade is: A')
elif score >= 80:
    print('Your grade is: B')
elif score >= 70:
    print('Your grade is: C')
elif score >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')




# program start
main()
