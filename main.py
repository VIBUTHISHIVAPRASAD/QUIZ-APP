import random

# Sample questions
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    # Add more questions
]

def run_quiz():
    score = 0
    random.shuffle(questions)

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

        user_answer = input("Your answer: ")
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
        print()

    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()

