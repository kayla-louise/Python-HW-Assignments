#Kayla Cook
#11-4 Astronomy Helper

#print menu
def print_menu () :
    print("Select a Planet")
    print
    print("1. Mercury")
    print("2. Venus")
    print("3. Earth")
    print("4. Mars")
    print("5. Exit the Program")
    selection = int(input("Enter your selection"))
    while selection < 1 or selection > 5:
        print("That is not a valid menu selection")
        selection = int(input("Enter your selection"))
    if selection == 1:
        mercury()
    elif selection == 2:
        venus()
    elif selection == 3:
        earth()
    elif selection == 4:
        mars()
    elif selection ==5:
        finish()
    else:
        print("An unknown error occurred, please try again")
        print_menu()

#mercury
def mercury() :
    print("All About Mercury!")
    print("===================")
    print("Average distance from the sun is:")
    print("57.9 million kilometers")
    print
    print("Mass is:   3.31 * 10^23  kg")
    print
    print("Surface temperature ranges from:")
    print("-173 degrees Celsius to 430 degrees Celsius")
    print
    print_menu()
#venus
def venus() :
    print("All About Venus!")
    print("===================")
    print("Average distance from the sun is:")
    print("108.2 million kilometers")
    print
    print("Mass is:   4.87 * 10^24  kg")
    print
    print("Surface temperature ranges from:")
    print("472 degrees Celsius")
    print
    print_menu()
#earth
def earth() :
    print("All About Earth!")
    print("===================")
    print("Average distance from the sun is:")
    print("149.6 million kilometers")
    print
    print("Mass is:   5.967 * 10^24  kg")
    print
    print("Surface temperature ranges from:")
    print("-50 degrees Celsius to 50 degrees Celsius")
    print
    print_menu()
#mars
def mars() :
    print("All About Mars!")
    print("===================")
    print("Average distance from the sun is:")
    print("227.9 million kilometers")
    print
    print("Mass is:   0.6424 * 10^24  kg")
    print
    print("Surface temperature ranges from:")
    print("-140 degrees Celsius to 20 degrees Celsius")
    print
    print_menu()
#quit
def finish() :
    print("Good Bye")
#call first module
print_menu()
