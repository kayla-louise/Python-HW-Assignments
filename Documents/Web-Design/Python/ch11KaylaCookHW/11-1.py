#Kayla Cook
#11-1 Language Translator

#print menu module
def print_module () :
    print("Welcome to the language translator")
    print("We will translate 'Good Morning'")
    print
    print("1.  English")
    print("2.  Italian")
    print("3.  Spanish")
    print("4.  German")
    print("5.  End Program")
    menu_selection = int(input("Enter your selection: "))
#validate menu selection
    while menu_selection < 1 or menu_selection > 5:
        print("That is not a valid menu selection")
        menu_selection = int(input("Enter your selection: "))
    if menu_selection == 1:
        option1()
    elif menu_selection == 2:
        option2()
    elif menu_selection == 3:
        option3()
    elif menu_selection == 4:
        option4()
    elif menu_selection == 5:
        option5()
    else:
        print("An unknown error has occurred, please try again")
        print_module()
#option 1 module
def option1() :
    print("Good Morning")
    print_module()
#option 2 module
def option2():
    print("Buongiorno")
    print_module()                            
#option 3 module
def option3() :
    print("Buenos Dias")
    print_module()
#option 4 module
def option4() :
    print("Guten Morgen")
    print_module()
#option 5 module
def option5() :
    print("Good Bye!")
#call first module
print_module()
