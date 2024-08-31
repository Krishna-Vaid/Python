import random
import time

operators = ["+", "-", "*",]
min_operand = 1
max_operand = 10
problems = 10


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    que = str(left) + " " + operator + " " + str(right)
    answer = eval(que)
    return que, answer


wrong = 0
input("Press enter to start :")
print("----------------------")

start_time = time.time()

for i in range(problems):
    que, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + que + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Good work! You finished problems in", total_time, "seconds!")
