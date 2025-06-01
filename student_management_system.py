from os import system
from pickle import dump, load


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


class student:
    def __init__(self):
        self.name = ""
        self.roll_no = ""
        self.dob = ""
        self.gender = ""
        self.phone_no = ""
        self.email = ""
        self.branch = ""
        self.course = ""
        self.semester = ""

    def __str__(self):
        return (
f"""---------------------------------
Student Name      : {self.name}
Student RollNo    : {self.roll_no}
Student Gender    : {self.gender}
Student DOB       : {self.dob}
Student Email-id  : {self.email}
Student Mobile No : {self.phone_no}
Student Branch    : {self.branch}
Student Course    : {self.course}
Student Semester  : {self.semester}
"""
)
    
class AuthData:
    def __init__(self):
        self.Name = None
        self.User_name = None
        self.Password = None
        self.Email_id = None


class Record_Auth_Data:
    def __init__(self):
        self.record = None
        self.auth = None


class Student_Record:
    def __init__(self):
        self.List_Student_Records = []
        self.auth_list = []
        self.login_username = ""
        self.login_password = ""

    def save_file(self):
        temp = Record_Auth_Data()
        temp.record = self.List_Student_Records
        temp.auth = self.auth_list
        with open("Student-DataBase.pkl", 'wb') as file:
            dump(temp, file)

    def load_file(self):
        try:
            with open("Student-DataBase.pkl", 'rb') as file:
                rowData = load(file)
                self.List_Student_Records = rowData.record
                self.auth_list = rowData.auth
        except FileNotFoundError:
            Red()
            print("File Reading Error")
        finally:
            Reset()
    
    def add_student_record(self):
        temp_data = student()
        Magenta()
        print("----------------------------------")
        temp_data.name      = input("Enter Student Name      : ")
        temp_data.roll_no   = input("Enter Student Roll No   : ")
        temp_data.dob       = input("Enter Student DOB       : ")
        temp_data.gender    = input("Enter Student Gender    : ")
        temp_data.phone_no  = input("Enter Student Mobile No : ")
        temp_data.email     = input("Enter Student Email-id  : ")
        temp_data.branch    = input("Enter Student Branch    : ")
        temp_data.course    = input("Enter Student Course    : ")
        temp_data.semester  = input("Enter Student Semester  : ")
        
        if (
            not temp_data.name      or
            not temp_data.roll_no   or
            not temp_data.dob       or
            not temp_data.gender    or
            not temp_data.phone_no  or
            not temp_data.email     or
            not temp_data.branch    or
            not temp_data.course    or
            not temp_data.semester
        ):
            Red()
            print("All fields are requried")
        else:
            self.List_Student_Records.append(temp_data)
            Green()
            print("New Record Add Successfully")
        Reset()

    def delete_student_record(self):
        Magenta()
        print("---------------------------------")
        roll_no = input("Enter Student Roll No : ")
        for data in self.List_Student_Records:
            if data.roll_no == roll_no:
                self.List_Student_Records.remove(data)
                Red()
                print("----------------------------")
                print("Deleted Student Record :-")
                print(data)
                break
        else:
            Red()
            print(f"{roll_no} is not found in the database")
        Reset()

    def update_student_record(self):
        Magenta()
        print("---------------------------------")
        roll_no = input("Enter Student Roll No : ")
        index = 0
        while index < len(self.List_Student_Records):
            data = self.List_Student_Records[index]
            if roll_no == data.roll_no:
                temp_data = student()
                temp_data.name      = input("Enter Student Name      : ")
                temp_data.dob       = input("Enter Student DOB       : ")
                temp_data.phone_no  = input("Enter Student Mobile No : ")
                temp_data.email     = input("Enter Student Email-id  : ")
                temp_data.branch    = input("Enter Student Branch    : ")
                temp_data.semester  = input("Enter Student Semester  : ")

                temp_data.roll_no  = roll_no
                temp_data.gender   = data.gender
                temp_data.course  = data.course
                
                if not temp_data.name:
                    temp_data.name = data.name
                
                if not temp_data.dob:
                    temp_data.dob = data.dob
        
                if not temp_data.phone_no:
                    temp_data.phone_no = data.phone_no
                
                if not temp_data.email:
                    temp_data.email = data.email

                if not temp_data.branch:
                    temp_data.branch = data.branch
                
                if not temp_data.semester:
                    temp_data.semester = data.semester

                self.List_Student_Records[index] = temp_data
                Green()
                print("----------------------------")
                print("Student Record Update Successfully")
                print("Updated Record :-")
                print(temp_data)
                break
            index += 1
        else:
            Red()
            print(f"{roll_no} is not found in the database")
        Reset()

    def search_by_roll_no(self):
        Magenta()
        print("---------------------------------")
        roll_no = input("Enter Student Roll No : ")
        for data in self.List_Student_Records:
            if data.roll_no == roll_no:
                print(data)
                break
        else:
            Red()
            print(f"{roll_no} is not found in the database")
        Reset()

    def search_by_email(self):
        Magenta()
        print("---------------------------------")
        email = input("Enter Student Roll No : ")
        for data in self.List_Student_Records:
            if data.email == email:
                print(data)
                break
        else:
            Red()
            print(f"{email} is not found in the database")
        Reset()

    def search_by_name(self):
        Magenta()
        print("---------------------------------")
        found = True
        name = input("Enter Student Name : ")
        for data in self.List_Student_Records:
            if data.name == name:
                print(data)
                found = False
        if found:
            Red()
            print(f"{name} is not found in the database")
        Reset()

    def search_by_gender(self):
        Magenta()
        print("---------------------------------")
        found = True
        gender = input("Enter Student Gender : ")
        for data in self.List_Student_Records:
            if data.gender == gender:
                print(data)
                found = False
        if found:
            Red()
            print(f"{gender} is not found in the database")
        Reset()

    def search_by_branch(self):
        Magenta()
        print("---------------------------------")
        found = True
        branch = input("Enter Student Branch : ")
        for data in self.List_Student_Records:
            if data.branch == branch:
                print(data)
                found = False
        if found:
            Red()
            print(f"{branch} is not found in the database")
        Reset()

    def search_by_course(self):
        Magenta()
        print("---------------------------------")
        found = True
        course = input("Enter Student Course : ")
        for data in self.List_Student_Records:
            if data.course == course:
                print(data)
                found = False
        if found:
            Red()
            print(f"{course} is not found in the database")
        Reset()

    def search_by_semester(self):
        Magenta()
        print("---------------------------------")
        found = True
        semester = input("Enter Student semester : ")
        for data in self.List_Student_Records:
            if data.semester == semester:
                print(data)
                found = False
        if found:
            Red()
            print(f"{semester} is not found in the database")
        Reset()

    def print_all_records(self):
        if len(self.List_Student_Records):
            Cyan()
            for data in self.List_Student_Records:
                print(data)
        else:
            Red()
            print("No Record in the database")
        Reset()
    
    def home_page(self):
        Green()
        print("Welcome to Student Record Management System")
        print("-------------------------------------------")
        while True:
            Blue()
            print("Enter 1  for Add New Record")            
            print("Enter 2  for Delete Record")
            print("Enter 3  for Update Record")
            print("Enter 4  for Search By Roll No")
            print("Enter 5  for Search By Name")
            print("Enter 6  for Search By Gender")
            print("Enter 7  for Search By Email")
            print("Enter 8  for Search By Branch")
            print("Enter 9  for Search By Course")
            print("Enter 10 for Search By Semester")
            print("Enter 11 for Dispaly All Records")
            print("Enter 12 for Logout this App")
            choice = int(input("Enter your choice : "))
            Reset()
            system("clear")
            match(choice):
                case 1:
                    self.add_student_record()
                    self.save_file()
                case 2:
                    self.delete_student_record()
                    self.save_file()
                case 3:
                    self.update_student_record()
                    self.save_file()
                case 4:
                    self.search_by_roll_no()
                case 5:
                    self.search_by_name()
                case 6:
                    self.search_by_gender()
                case 7:
                    self.search_by_email()
                case 8:
                    self.search_by_branch()
                case 9:
                    self.search_by_course()
                case 10:
                    self.search_by_semester()
                case 11:
                    self.print_all_records()
                case 12:
                    system("clear")
                    print("Logout")
                    break
                case _:
                    print("Invalid your choice")

    def Register(self):
        temp_data = AuthData()
        temp_data.Name =      input("Enter Full Name : ")
        temp_data.User_name = input("Enter  UserName : ")
        temp_data.Password =  input("Enter Password  : ")
        temp_data.Email_id =  input("Enter Email id  : ")
        self.load_file()
        for _ in self.auth_list:
            if _.User_name == temp_data.User_name and _.Email_id == temp_data.Email_id:
                Red()
                print("UserName is already exist")
                break
        else:
            self.auth_list.append(temp_data)
            self.save_file()
            Green()
            print("User Register Successfully")
            self.home_page()
        Reset()

    def Login(self):
        User_name = input("Enter  UserName : ")
        Password =  input("Enter Password  : ")
        self.load_file()
        for _ in self.auth_list:
            if _.User_name == User_name and _.Password == Password:
                self.login_username = User_name
                self.login_password = Password
                self.home_page()
                self.login_username = ""
                self.login_password = ""
                break
        else:
            Red()
            print("Invalid username and password")
        Reset()

    def login_home_page(self):
        print("Welcome to Login page")
        while(True):
            Cyan()
            print("Enter 1 for register user")
            print("Enter 2 for login user")
            print("Enter 3 for Exit this App...!")
            choice = int(input("Enter your choice : "))
            system("clear")
            match(choice):
                case 1:
                    self.Register()
                case 2:
                    self.Login()
                case 3:
                    system("clear")
                    Blue()
                    print("Thank you for using App")
                    break
                case _:
                    print("Invalid choice")

obj  = Student_Record()
obj.login_home_page()