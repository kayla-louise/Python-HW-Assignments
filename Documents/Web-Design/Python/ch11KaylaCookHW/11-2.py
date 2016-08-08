#Kayla Cook
#11-2 University Meal Plan Selector

#print menu
def print_menu() :
    print("Welcome to the University Meal Plan Calculator")
    print("Plan #1 : 7 meals per week for $560 per semester")
    print("Plan #2 : 14 meals per week for $1,095 per semester")
    print("Plan #3 : Unlimited meals for $1,500 per semester")
    print("Type '4' to exit")
    menu_selection = int(input("Please enter the number for the plan you want:"))
    while menu_selection < 1 or menu_selection > 4:
        print("That is not a valid menu selection")
        menu_selection = int(input("Please enter the number for the plan you want:"))
#get num semesters
    num_semesters = int(input("Please enter the number of semesters: "))
#plan 1
    if menu_selection == 1 :
        plan1(num_semesters)
#plan 2
    elif menu_selection == 2 :
        plan2(num_semesters)
#plan 3
    elif menu_selection == 3 :
        plan3(num_semesters)
#escape
    elif menu_selection == 4:
        plan4()
    else:
        print("An unknown error has occurred, please try again")
        print_menu()
#plan1 module
def plan1(num_semesters) :
    total_cost = (num_semesters * 560)
    print("With meal plan #1, the cost for ", num_semesters, " semesters is : ")
    print("$", format(total_cost, '.2f'))
    print_menu()
#plan2 module
def plan2(num_semesters) :
    total_cost = (num_semesters * 560)
    print("With meal plan #2, the cost for ", num_semesters, " semesters is : ")
    print("$", format(total_cost, '.2f'))
    print_menu()
#plan3 module
def plan3(num_semesters) :
    total_cost = (num_semesters * 560)
    print("With meal plan #3, the cost for ", num_semesters, " semesters is : ")
    print("$", format(total_cost, '.2f'))
    print_menu()
#plan4 module/escape
def plan4() :
    print("Good Bye")
#call print menu module
print_menu()
