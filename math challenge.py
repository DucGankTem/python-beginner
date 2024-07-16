import random
import time


OPERATOR = ["+", "-", "/", "*"]
MIN_OPERAND = 0
MAX_OPERAND = 10
TOTAL_PROBLEM = 10 

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATOR)

    expr = str(left) +" "+ operator +" "+ str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #"+ str(i + 1) + ": "+ expr +" = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("----------------")
print("Nice work You finished in", total_time, "seconds!")