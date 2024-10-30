#python quiz game

questions = ("How many elements in the p table?: ",
              "which animal lays th ebig egg?: ",
              "what is the most abundant gas on earf?: ",
              "How many bones in da body?: ",
              "What the hottest planet in this so sys?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 1123"),
           ("A. cat", "B. dog", "C. bird", "D. Ostrich"),
           ("A. Nitrogen", "B. farts", "C. more farts", "D. the most farts"),
           ("A. 206", "B. 2", "C. 3", "D. 4"),
           ("A. Merc", "B. Venus", "C. Earf", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("\nCORRECT FUCK HEAD!\n")
        score += 1
    else:
        print("\nINCORRECT IDIOT!\n")
    
    question_num += 1

print("-------------------------------")
print("            RESULTS            ")
print("-------------------------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"your score is {score} percent")
