questions = (
    "Q1.print(type('Hello World!))",
    "Q2. Which of the following is a correct variable name in Python?",
    "Q3. print(5 // 2)",
    "Q4. x = {'name': 'Alice', 'age': 25}",
    "Q5. Which keyword is used to define a function in Python?",
    "Q6. What does the len() function do in Python?",
    "Q7. x = [1, 2, 3]  print(x[1])",
    "Q8. Which operator is used for exponentiation in Python?",
    "Q9. Which of the following is not a mutable data type in Python?",
    "Q10. Which of the following statements is used to handle exceptions in Python?"
    "Q11. which of the following is  a mutable data type in python?"
)
options = (
    (
        "A. <class 'int'>",
        "B. <class 'str'>",
        "C. <class 'list'>",
        "D. <class 'bool'>"
),
(
    "A. 2name",
    "B. my-name",
    "C. my_name",
    "D. my name"
),
(
    "A. 2.5",
    "B. 2",
    "C. 3",
    "D. Error"
),
(
    "A. List",
    "B. Tuple",
    "C. Dictionary",
    "D. Set"
),
(
    "A. function",
    "B. fun",
    "C. def",
    "D. define"
),
(
    "A. Returns the size of file",
    "B. Returns the number of characters or items",
    "C. Returns memory address",
    "D. None of the above"
),
(
    "A. 1",
    "B. 2",
    "C. 3", 
    "D. Error"
),
(
    "A. ^",
    "B. %",
    "C. **",    
    "D. //"
),
(
    "A. List",
    "B. Dictionary",
    "C. Tuple",
    "D. Set"
),
(
    "A. try-catch",
    "B. try-catch-finally",
    "C. try-except",
    "D. do-except"
)
)
    "A. string",
    "B. tuple" ,
    "C. number",
    "D. set" ,
answers = ('B','C','B','C','C','B','B','C','C','C','D')
guesses = []
question_num = 0
score = 0
for question in questions:
    print("---------------------------------------------------------------------------------")
    print(question)
    print("----------------------------------------------------------------------------------")
    for option in options[question_num]:
        print(option)
    guess = input("Enter A. B. C. D: ").upper()
    if guess==answers[question_num]:
        guesses.append(guess)
        print("Correct")
        score +=1
    else:
        guesses.append(guess)
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("-------------------------------------------------------------")
print("                        RESULT                               ")
print("-------------------------------------------------------------")
print("Answers", end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("Guesses", end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
if len(guesses)!=0:
    print("Your Score :",(score/len(guesses))*100,"%")
else:

    print("Your Score : 100%")
