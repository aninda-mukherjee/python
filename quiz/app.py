from Question import Question
question_prompts = [
    "What color are appleas?\n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color Bananas?\n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color are Strawberries?\n(a) Red/Green \n(b) Purple \n(c) Orange \n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got :" +str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)