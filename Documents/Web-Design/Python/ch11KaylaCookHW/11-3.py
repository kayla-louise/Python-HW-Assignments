#Kayla Cook
#11-3 Geometry Calculator
#global constants
pi = 3.14159
#print menu
def print_menu() :
    print("Welcome to The Geometry Calculator")
    print("1. Calculate the Area of a Circle")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Triangle")
    print("4. Quit")
    menu_selection = int(input("Enter your menu selection: "))
    while menu_selection <1 or menu_selection > 4:
        print("That is not a valid menu selection")
        menu_selection = int(input("Enter your menu selection: "))
    if menu_selection == 1:
        radius = float(input("Please enter the radius of the circle : "))
        areaCircle(radius)
    if menu_selection == 2:
        length = float(input("Please enter the length of the rectangle : "))
        width = float(input("Please enter the width of the rectangle : "))
        areaRectangle(length, width)
    if menu_selection == 3:
        base = float(input("Please enter the length of the triangle's base : "))
        height = float(input("Please enter the height of the triangle : "))
        areaTriangle(base, height)
    if menu_selection == 4:
        quit_module()
#area circle
def areaCircle(radius):
    area = (pi * (radius * radius))
    print("The area of the circle is : ", area)
    print_menu()
#area rectangle
def areaRectangle(length, width):
    area = (length * width)
    print("The area of the rectangle is : ", area)
    print_menu()
#area triangle
def areaTriangle(base, height):
    area = (base * height * 0.5)
    print("The area of the triangle is : ", area)
    print_menu()
#quit
def quit_module():
    print("Good Bye")
#call first module
print_menu()
