print("Welcome to quiz competition")

playing = input("Do you want to play? : ")

if playing.upper() != "YES":
   quit()


print("Okay! Let's play :)")

score = 0

answer = input("What does DNA stand for? ")
if answer.upper() == "DEOXYRIBONUCLEIC ACID":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which gas is most abundant in the Earth's atmosphere? ")
if answer.upper() == "NITROGEN":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which river is the longest in the world? ")
if answer.upper() == "NILE":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which planet in our solar system is known as the Red Planet? ")
if answer.upper() == "MARS":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")