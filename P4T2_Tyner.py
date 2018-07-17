# P4T2
# Bug Collector
# Layton Tyner
# 28 Jun 2018


# initialize my accumulator to zero
total = 0

# run for loop to get the total
for day in range(1,8):
        # sep="" removes spaces around the variable
        # end="" keeps you on the same line
        print("Enter number of insects collected on day ",day,": ",sep="",end="")
        insects = int(input())
        #insects = int(input("Enter insects collected: "))
        # two options; total += insects or total = total + insects 
        total += insects                   
print("The insect total collected for seven days is ",format(total,',.0f'))

average = total/day

print("The daily average is",format(average,',.0f'))
