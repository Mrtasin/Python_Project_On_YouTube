from random import random
from datetime import datetime
from pickle import dump, load
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

class Task:
    def __init__(self):
        self.title       = ""
        self.description = ""
        self.status      = False
        self.deu_date    = ""
        self.task_id     = int(random()*1000000)
        self.createdAt   = datetime.now()

    def __str__(self):
        return (
f"""\033[36m--------------------------------
Task id No       : {self.task_id}
Task Title       : {self.title}
Task Description : {self.description}
Task Status      : {"Completed" if self.status else "Pending"}
Task Due Date    : {self.deu_date}
Task createdAt   : {self.createdAt} \033[0m
"""
        )
    
class Auth:
    def __init__(self):
        self.Name = None
        self.User_name = None
        self.Password = None
        self.Email_id = None
    

class task_auth:
    def __init__(self, tasks, username, password, auth):
        self.Tasks = tasks
        self.username = username
        self.password = password
        self.auth     = auth


class Task_Manager:
    def __init__(self):
        self.List_of_task = []
        self.login_username = ""
        self.login_password = ""
        self.auth = ""
    
    def add_task(self):
        tempData = Task()
        print("------------------------------")
        tempData.title       = input("Enter Task Title               : ")
        tempData.description = input("Enter Task Description         : ")
        tempData.deu_date    = input("Enter Task Due_Date(DD/MM/YYYY): ")
        self.List_of_task.append(tempData)
        print("------------------------------")
        print("Add Task Successfully")
        print(tempData)

    def update_task(self):
        task_id = int(input("Enter Task Id : "))
        index = 0
        while(index < len(self.List_of_task)):
            temptask = self.List_of_task[index]
            if( task_id == temptask.task_id ):
                title       = input("Enter Task Title               : ")
                description = input("Enter Task Description         : ")
                deu_date    = input("Enter Task Due_Date(DD/MM/YYYY): ")
                
                temptask.title       = title if title else temptask.title
                temptask.description = description if description else temptask.description
                temptask.deu_date    = deu_date if deu_date else temptask.deu_date

                self.List_of_task[index] = temptask
                Green()
                print("Update Successfully")
                print(temptask)
                break

            index += 1
        else:
            Red()
            print("Task id is not found in the database")
        Reset()

    def delete_task(self):
        task_id = int(input("Enter Task Id : "))
        for task in self.List_of_task:
            if(task_id == task.task_id):
                self.List_of_task.remove(task)
                print("Deleteing Successfully")
                print(task)
                break
        else:
            Red()
            print("Task id is not found in the database")
        Reset()

    def search_by_id(self):
        task_id = int(input("Enter Task Id : "))
        for task in self.List_of_task:
            if(task_id == task.task_id):
                print(task)
                break
        else:
            Red()
            print("Task id is not found in the database")
        Reset()

    def search_by_title(self):
        title = input("Enter Task Title : ")
        for task in self.List_of_task:
            if(title == task.title):
                print(task)
                break
        else:
            Red()
            print("Task id is not found in the database")
        Reset()

    def print_complete_task(self):
        for task in self.List_of_task:
            if task.status:
                print(task)
    
    def print_pending_task(self):
        for task in self.List_of_task:
            if not task.status:
                print(task)
    
    def print_all_task(self):
        for task in self.List_of_task:
                print(task)

    def save_file(self):
        with open(self.login_username+".pkl", 'wb') as file:
            data = task_auth(self.List_of_task,self.login_username,self.login_password,self.auth)
            dump(data, file)


    def load_file(self,username):
        try:
            with open(username+".pkl", 'rb') as file:
                data = load(file)
                self.List_of_task   = data.Tasks
                self.login_username = data.username
                self.login_password = data.password
                self.auth           = data.auth
        except FileNotFoundError:
            Red()
            print("File Not Found Error")

    def home_page(self):
        while(True):
            Magenta()
            print(f"Welcome {self.auth.Name} to Task Manager")
            Blue()
            print("--------------------------------")
            print("1. Add Task")
            print("2. Update Task")
            print("3. Delete Task")
            print("4. Search by Id")
            print("5. Search by Title")
            print("6. Print Complete Task")
            print("7. Print Pending Task")
            print("8. Print All Task")
            print("9. Logout")
            choice = int(input("Enter your choice : "))
            system("clear")
            match(choice):
                case 1:
                    self.add_task()
                    self.save_file()
                case 2:
                    self.update_task()
                    self.save_file()
                case 3:
                    self.delete_task()
                    self.save_file()
                case 4:
                    self.search_by_id()
                case 5:
                    self.search_by_title()
                case 6:
                    self.print_complete_task()
                case 7:
                    self.print_pending_task()
                case 8:
                    self.print_all_task()
                case 9:
                    print("Logout")
                    self.login_username = ""
                    self.login_password = ""
                    break
                case _:
                    Red()
                    print("Invalid Choice")
            Reset()

    def Register(self):
        authData = Auth()
        authData.Name =      input("Enter Full Name : ")
        authData.User_name = input("Enter UserName  : ")
        authData.Password =  input("Enter Password  : ")
        authData.Email_id =  input("Enter Email id  : ")
        try:
            with open(authData.User_name + ".pkl", 'rb') as Data:
                print("UserName is already exist")
        except FileNotFoundError:
            self.auth = authData
            self.login_username = authData.User_name
            self.login_password = authData.Password
            self.save_file()
            print("User Register Successfully")
            self.home_page()


    def Login(self):
        User_name = input("Enter  UserName : ")
        Password =  input("Enter Password  : ")
        self.load_file(User_name)
        if(User_name == self.login_username and Password == self.login_password):
            self.home_page()
        else:
            print("username and password invalid")

    def auth_home_page(self):
        Cyan()
        print("Welcome to To-Do List App")
        while(True):
            print("--------------------------------")
            print("Enter 1. for Login")
            print("Enter 2. for Register")
            print("Enter 3. for Exit...!")
            choice = int(input("Enter your choice : "))
            system('clear')
            match(choice):
                case 1:
                    self.Login()
                case 2:
                    self.Register()
                case 3:
                    print("Thank you using Task Manager")
                    break
                case _:
                    Red()
                    print("Invalid Choice")        


obj = Task_Manager()

obj.auth_home_page()