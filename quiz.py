# Quiz Application

score = 0

questions = {
    "What is the capital of India?": "B",
    "Which language is used for Python programming?": "A",
    "What is 5 + 5?": "C",
    "Who is known as the Father of Computers?": "D",
    "Which planet is known as the Red Planet?": "B"
}

options = [
    ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
    ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    ["A. 8", "B. 9", "C. 10", "D. 11"],
    ["A. Albert Einstein", "B. Newton", "C. Tesla", "D. Charles Babbage"],
    ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"]
]

question_num = 0

print("===== QUIZ APPLICATION =====")

for question in questions:
    print("\n" + question)

    for option in options[question_num]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == questions[question]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {questions[question]}")

    question_num += 1

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n===== QUIZ RESULT =====")
print(f"Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 50:
    print("Grade E")
else:
    print("Fail")