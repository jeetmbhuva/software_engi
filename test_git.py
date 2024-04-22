import random

class Student:
    def __init__(self, n, r):
        self.name = n
        self.rounds = r
        self.score = 0

    def display(self):
        print(self.name)

    def greet(self):
        print("Hello" + self.name + "!!")

class Addition:
    def __init__(self):
        self.number1 = random.randint(1, 10)
        self.number2 = random.randint(1, 10)
        self.result = self.number1 + self.number2

    def check_result(self, guess):
        if guess == self.result:
            return True
        else:
            return False

    def get_question(self):
        return f'what is {self.number1} + {self.number2 }? '

inp_name = input("whats your name?  ")
inp_rounds = input("how many rounds do you want to do?")

student1 = Student(inp_name, int(inp_rounds))
student1.greet()

for i in range(1, student1.rounds + 1):
    question = Addition()
    print(question.get_question())
    inp_guess = input()
    if question.check_result(int(inp_guess)):
        student1.score += 1
        print('correct')
    else:
        print('wrong')

print(f'you answered {student1.score} out of {student1.rounds} correctly.')