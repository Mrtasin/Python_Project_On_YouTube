import random
from os import system

def Red():
    print("\033[31m", end='')

def Green():
    print("\033[32m", end='')

def Yellow():
    print("\033[33m", end='')

def Blue():
    print("\033[34m", end='')

def Magenta():
    print("\033[35m", end='')

def Cyan():
    print("\033[36m", end='')

def Reset():
    print("\033[0m", end='')

def Bold():
    print("\033[1m", end='')

def Underline():
    print("\033[4m", end='')


class Question:
    def __init__(self):
        self.question = ""
        self.OptionA = ""
        self.OptionB = ""
        self.OptionC = ""
        self.OptionD = ""
        self.answer = ""

def load_file(filename = "Quiz.txt"):
    try:
        list_of_questions = []
        with open(filename, 'r') as file:
            temp_ques = []
            for line in file.readlines():
                if line == "":
                    continue
                temp_ques.append(line.strip())
                if len(temp_ques) == 6:
                    question = Question()
                    question.question = temp_ques[0]
                    question.OptionA  = temp_ques[1]                    
                    question.OptionB  = temp_ques[2]
                    question.OptionC  = temp_ques[3]
                    question.OptionD  = temp_ques[4]       
                    question.answer   = temp_ques[5]
                    list_of_questions.append(question)
                    temp_ques = []
        return list_of_questions
    
    except FileNotFoundError:
        print(f"{filename} is not Found")

def add_question_to_file(question, filename = "Quiz.txt"):
    with open(filename, 'a') as file:
        file.write(question.question + "\n")
        file.write(question.OptionA  + "\n")
        file.write(question.OptionB  + "\n")
        file.write(question.OptionC  + "\n")
        file.write(question.OptionD  + "\n")
        file.write(question.answer   + "\n")
        


class Quiz_App:
    def __init__(self, name):
        self.list_of_questions = load_file()
        self.Name = name
        self.score = 0
        self.correct_ans = 0
        self.wrong_ans = 0
    
    def print_question(self, q):
        print("----------------------------")
        print(q.question)
        Magenta()
        print(f"A : {q.OptionA}  \t  B : {q.OptionB}")
        print(f"C : {q.OptionC}  \t  D : {q.OptionD}")
        Reset()

    def show_question(self):
        print("Number of questions are : 5")
        temp_list = random.sample(self.list_of_questions, len(self.list_of_questions))
        counter = 0
        for que in temp_list:
            
            self.print_question(que)
            Blue()
            ans = input("Enter Correct Ans : ")
            system("clear")
            if ans.lower() == que.answer.lower():
                Green()
                print("Correct Ans")
                self.correct_ans += 1
            else:
                Red()
                print("Worng Ans")
                self.wrong_ans += 1
            Reset()
            counter += 1

            if counter == 5:
                break

    def result(self):
        total = self.correct_ans + self.wrong_ans
        self.score = self.correct_ans
        Blue()
        print("--------------------------")
        print(f"Name : {self.Name}")
        print(f"Total Score : {self.score}/{total}")
        Green()
        print(f"Total Correct Answer : {self.correct_ans}")
        Red()
        print(f"Total Worng Answer : {self.wrong_ans}")
        Reset()

    def main_menu(self):
        self.show_question()
        self.result()


obj = Quiz_App("Tasin Bhai")
obj.main_menu()