#Kayla Cook
#8-8 Payroll

#empId array
empId = [56588, 45201, 78951, 87775, 84512, 13028, 75804]
#hours array
hours = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
#payRate array
payRate = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
#wages array
wages = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
#set initial index
index = 0
#display empId and ask for hours and payrate
while index < len(empId):
    print("Please enter the hours worked by the employee with the ID# :", empId[index])
    hours[index] = float(input(" : ")) 
    print("Please enter the pay rate of the employee with the ID# :", empId[index])                            
    payRate[index] = float(input(" : "))
    index = index + 1
#counter for second loop
count = 0
#calculate wages and display
while count < len(wages):
    wages[count] = float((hours[count]) * (payRate[count]))
    print("Employee id:", empId[count], " | gross wages are $", (format(wages[count], '.2f')))
    count = (count + 1)

