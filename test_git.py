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

class Arithmetic: 
    def __init__(self):
        super().__init__()
        self.r1 = random.randint(1,10)
        self.r2 = random.randint(1,10)
        self.number1 = 0
        self.number2 = 0
        self.symbol = "0"

    def check_result(self, guess):
        if guess == self.result:
            return True
        else:
            return False
        

class Multiplication (Arithmetic):
    def __init__(self):
        super().__init__()
        self.number1 = self.r1
        self.number2 = self.r2 
        self.result  = self.number1 * self.number2
        self.symbol = "x"
        


class Addition (Arithmetic):
    def __init__(self):
        super().__init__()
        self.number1 = self.r1
        self.number2 = self.r2
        self.result = self.number1 + self.number2
        self.symbol = "+"

    def get_question(self):
        return f'what is {self.number1} + {self.number2}? '

class Subtraction (Arithmetic):
    def __init__(self):
        super().__init__()
        if self.r1 < self.r2:
           self.number1 = self.r2
           self.number2 = self.r1  
        else:
            self.number1 = self.r1
            self.number2 = self.r2
        self.result = self.number1 - self.number2
        self.symbol = "-"

    def check_result(self, guess):
        if guess == self.result:
            return True
        else:
            return False

    def get_question(self):
        return f'what is {self.number1} {self.symbol} {self.number2}? '

inp_name = input("whats your name?  ")
inp_rounds = input("how many rounds do you want to do?")

student1 = Student(inp_name, int(inp_rounds))
student1.greet()

for i in range(1, student1.rounds + 1):
    choice = random.randint(1, 3)
    if choice == 1:
        question = Addition()
    elif choice == 2:
        question = Multiplication()
    elif choice == 3:
        question = Subtraction()

    inp_guess = input(question.get_question())
    if question.check_result(int(inp_guess)):
        student1.score += 1
        print('correct')
    else:
        print('wrong')

print(f'you answered {student1.score} out of {student1.rounds} correctly.')