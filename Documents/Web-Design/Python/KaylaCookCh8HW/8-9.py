#Kayla Cook
#8-9 Drivers License Exam

#correct answer array
correct_answers = ['B', 'D', 'A', 'A', 'C',
                   'A', 'B', 'A', 'C', 'D',
                   'B', 'C', 'D', 'A', 'D',
                   'C', 'C', 'B', 'D', 'A']
#student answer array
student_answers = ['X', 'X', 'X', 'X', 'X',
                   'X', 'X', 'X', 'X', 'X',
                   'X', 'X', 'X', 'X', 'X',
                   'X', 'X', 'X', 'X', 'X']
#get student answers
print("Please turn CAPS LOCK ON! Student answers should be capital letters")
index = 0
while index < len(student_answers):
    student_answers[index] = input("Enter the student's answer for question" +
                                   str(index +1) + " : ")
    index += 1
#create array to store incorrect answers
wrong_questions = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
#compare answers
count = 0
num_correct = 0
while count < len(student_answers):
    if student_answers[count] == correct_answers[count] :
        num_correct = num_correct + 1
        count += 1
    else:
        wrong_questions[count] = (count + 1)
        count +=1
#determine pass or fail
num_wrong = (20 - num_correct)
print("The number of correctly answered questions is : ", num_correct)
print("The number of incorrectly answered questions is : ", num_wrong)
if num_correct >= 15 :
    print("Congratulations, you have passed!")
else:
    print("Sorry, you did not pass. Better luck next time!")
#incorrect questions
print("Here are the questions you got wrong :")
arrayLoop = 0
while arrayLoop < len(wrong_questions):
    if wrong_questions[arrayLoop] > 0:
        print("Question #", (arrayLoop +1))
        arrayLoop = arrayLoop + 1
    else:
        arrayLoop = arrayLoop + 1
