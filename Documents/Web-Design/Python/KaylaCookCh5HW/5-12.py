#Kayla Cook
#5-12 factorals

#global
factorial = 1
#get a number
print("Hello and welcome to the factoral calculator!")
end = int(input("Please enter a non-negative number : "))

#calculate factoral
for i in range(1, end + 1):
    factorial = (factorial * i)
print("The factoral of ", end, " is ", factorial)
