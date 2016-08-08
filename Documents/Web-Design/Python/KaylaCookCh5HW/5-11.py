#Kayla Cook
#5-11 First and Last

#global variables
firstAlpha = 'A'
lastAlpha = 'z'
another = 'y'

#get the first name
print("Welcome to the alphabetical order generator!")
name = input("Please enter a name : ")
firstAlpha = name
lastAlpha = name
while another == 'y' or another == 'Y' :
    
    name = input("Please enter another name: ")
    
    if name < firstAlpha:
            firstAlpha = name
    elif name > lastAlpha :
            lastAlpha = name
    another = input("Do you have another name to enter? type y for yes")
        
    

        
#once there are no more names
print("The first name alphabetically is ", firstAlpha)
print("The last name alphabetically is ", lastAlpha)
