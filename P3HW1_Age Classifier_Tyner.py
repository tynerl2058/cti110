#CTI-110
#P3HW1 - Age Classifier
#Layton Tyner
#21 Jun 2018

# Given a persons age in years determine what their age classifier is

# Use the if/else structure to determine age classification

# Get input from the user

ageClassifier = float(input("Give the persons age in years (no months, give decimal if less than one) "))

if ageClassifier <= 1 and ageClassifier < 101:
    print("If the persons age is",ageClassifier,"they are an infant and you have many sleepless nights.")
elif ageClassifier >= 1 and ageClassifier < 13:
    print("If the persons age is",ageClassifier,"they are a child; enjoy this time.")
elif ageClassifier >= 13 and ageClassifier < 20:
    print("If the persons age is",ageClassifier,"they are a teenager; our prayers are with you.")
else:
    print("If the persons age is",ageClassifier,"they are a adult and they need to get a job.")
