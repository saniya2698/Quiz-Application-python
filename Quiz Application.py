# Python Quiz Application

questions = {
    "1. Who created Python?":
        ["A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Bjarne Stroustrup", "A"],

    "2. Which symbol is used for comments in Python?":
        ["A. //", "B. <!-- -->", "C. #", "D. /* */", "C"],

    "3. Which function is used to display output in Python?":
        ["A. display()", "B. print()", "C. output()", "D. show()", "B"],

    "4. Which data type is used for decimal numbers?":
        ["A. int", "B. str", "C. bool", "D. float", "D"],

    "5. Which keyword is used to define a function?":
        ["A. function", "B. define", "C. def", "D. fun", "C"],

    "6. Which operator is used for exponentiation in Python?":
        ["A. **", "B. ^", "C. //", "D. %", "A"],

    "7. Which of the following is a mutable data type?":
        ["A. tuple", "B. string", "C. list", "D. int", "C"],

    "8. Which keyword is used to create a loop in Python?":
        ["A. repeat", "B. for", "C. loop", "D. iterate", "B"],

    "9. Which function is used to take input from the user?":
        ["A. get()", "B. read()", "C. scan()", "D. input()", "D"],

    "10. What is the correct file extension of Python files?":
        ["A. .py", "B. .java", "C. .cpp", "D. .html", "A"],

    "11. Which keyword is used for conditional statements?":
        ["A. when", "B. if", "C. check", "D. select", "B"],

    "12. Which data type stores True or False values?":
        ["A. bool", "B. float", "C. str", "D. list", "A"],

    "13. Which operator is used for floor division?":
        ["A. /", "B. %", "C. //", "D. **", "C"],

    "14. Which function returns the length of a list or string?":
        ["A. size()", "B. count()", "C. length()", "D. len()", "D"],

    "15. Which keyword is used to import modules in Python?":
        ["A. include", "B. import", "C. using", "D. package", "B"],

    "16. Which of the following is a Python collection?":
        ["A. set", "B. integer", "C. float", "D. character", "A"],

    "17. Which keyword is used to exit a loop?":
        ["A. stop", "B. exit", "C. continue", "D. break", "D"],

    "18. Which function converts a string into an integer?":
        ["A. float()", "B. str()", "C. int()", "D. bool()", "C"],

    "19. Which keyword is used to create a class in Python?":
        ["A. object", "B. class", "C. define", "D. create", "B"],

    "20. Which operator is used to check equality?":
        ["A. =", "B. !=", "C. ==", "D. is", "C"]
}

score = 0
question_number = 1

print("===== Quiz Application =====")

for question in questions:
    print("\nQuestion", question_number)
    print(question)

    options = questions[question]

    for i in range(4):
        print(options[i])

    answer = input("Enter your answer (A/B/C/D): ")
    answer = answer.upper()

    if answer == options[4]:
        print("Correct Answer!")
        score = score + 1
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", options[4])

    question_number = question_number + 1

print("\n===== QUIZ RESULT =====")
print("Total Questions :", len(questions))
print("Correct Answers :", score)
print("Wrong Answers :", len(questions) - score)
print("Final Score :", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage :", percentage, "%")