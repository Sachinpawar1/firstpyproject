  print("Welcome to my computer quiz")

playing = input("Do you want to play? ").lower()
score = 0


if playing != "yes":
    print("See you!")
    quit()
else:
    print("Okay! Let's play :) ")

# Question num 1
answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect")

# Question num 2
answer = input("What does GPA stand for? ").lower()
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect")

# Question num 3
answer = input("Who is the Prime Minister of India? ").lower()
if answer == "narendra modi":
    print('correct!')
    score += 1
else:
    print("incorrect")

# Question num 4
answer = input("What is the capital of India? ").lower()
if answer == "new delhi":
    print('correct!')
    score += 1
else:
    print("incorrect")


print(f'You got {score} questions correct!')
print("You got " + str((score/4) * 100) + "%.")




