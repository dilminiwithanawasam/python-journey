# Quiz Game
print("Welcome to the Quiz Game!")
question_bank=[
    {
        "question": "What is the capital of France?","answers": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],"correct": "A"
    },
    {
        "question": "What is 2 + 2?","answers": ["A. 3", "B. 4", "C. 5", "D. 6"],"correct": "B"
    },
    {
        "question": "What is the largest planet in our solar system?","answers": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],"correct": "C"
    },
]
score=0

for item in question_bank:
    print(item["question"], item["answers"])
    user_answer=input("Your answer (A/B/C/D): ").upper()
    if user_answer==item["correct"]:
      print("Correct!\n")
      score+=1
    else:
      print("Wrong!\n")
      
print(f"Your final score is {score}/{len(question_bank)}.")