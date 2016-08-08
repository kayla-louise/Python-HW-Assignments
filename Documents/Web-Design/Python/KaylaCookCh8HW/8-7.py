#Kayla Cook
#8-7 Phone Number Lookup

#people array
people = ['Cody Parker', 'Shazia Sayeed', 'Elizabeth Lakoduk', 'Katlyn Sarnosky',
          'Brittany Gire', 'Kristopher Polakowski', 'Ryan James']

#phone-Numbers array
phone_Numbers = ['303-518-5555', '970-323-5555', '503-581-5555', '630-251-5555',
                 '209-477-5555', '719-660-5555', '720-870-5555' ]
#boolean variable to control loop
found = False
#loop counter
index = 0
#get name from user
search_Name = input('Please enter the name to search for :')
#step through array
while found ==False and index < len(people):
    if people[index] == search_Name :
        found = True
    else:
        index = index + 1

#display search results
if found:
    print('The phone number for ', search_Name, ' is : ', phone_Numbers[index])
else:
    print("Sorry, that name was not found, it's possible the spelling you provided was incorrect")
