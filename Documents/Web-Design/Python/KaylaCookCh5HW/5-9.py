#Kayla Cook
#5-9 Pennies Salary

#global variables
dayTotal = 0.005

#accumulator variables
total = 0.0
loopCount = 0

#gets days worked
daysWorked = int(input("How many days did you work?"))

#calculations loop
for counter in range(daysWorked):
   dayTotal = dayTotal + dayTotal
   total = total + dayTotal
   loopCount = loopCount + 1
   print("Day: ", loopCount, " Salary $ ", dayTotal)

#display total
print("The total salary is $", total)
   
