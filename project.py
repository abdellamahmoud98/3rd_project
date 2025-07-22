#list of questions and answers
#store the answers
#randomly pick questions
#ask ee if they are correct
# keep track of score
#tell the user their score at the end


import random


questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store a sequence of characters in Python?": "str",
    "What is the output of print(2 ** 3)?": "8",
    "How do you start a comment in Python?": "#",
    "What keyword is used to create a class in Python?": "class",
    "What is the name of the Python package manager?": "pip",
    "Which keyword is used to handle exceptions in Python?": "try",
    "What is the method to add an item to a list in Python?": "append",
    "What is the keyword used to import modules in Python?": "import",
    "What is the output of len([1, 2, 3])?": "3",
    "What is the keyword to define a variable in Python?": "var",
    "What is the method to convert a string to lowercase in Python?": "lower",
    "What is the keyword to define a loop in Python?": "for",
    "What is the method to remove an item from a list in Python?": "remove",
    "What is the output of 10 % 3?": "1",
    "What is the keyword to define a conditional statement in Python?": "if",
    "What is the method to sort a list in Python?": "sort",
    "What is the keyword to define a constant in Python?": "const"
}


def python_trivia_game():
    queastions_list = list(questions.keys())
    total_queasions = 5
    score = 0
    
    selected_questions = random.sample(queastions_list, total_queasions)
    
    for idx, question in enumerate(selected_questions):
        print(f"Question {idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        
        correct_answer = questions[question].lower().strip()

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}. \n")
    
    print(f"Your final score is {score} out of {total_queasions}.")
    
    
    
    
    
    
    
    
    
    
    
python_trivia_game()