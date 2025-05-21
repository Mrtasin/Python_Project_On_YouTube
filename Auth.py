class Auth:
    def __init__(self):
        self.Name = None
        self.User_name = None
        self.Password = None
        self.Email_id = None

    def Register(self):
        self.Name =      input("Enter Full Name : ")
        self.User_name = input("Enter  UserName : ")
        self.Password =  input("Enter Password  : ")
        self.Email_id =  input("Enter Email id  : ")
        try:
            with open(self.User_name + ".txt", 'r') as Data:
                print("UserName is already exist")
        except FileNotFoundError:
            with open(self.User_name + ".txt", 'w') as Data:
                Data.write(self.Name + "\n" + self.User_name + "\n" + self.Password + "\n" + self.Email_id)
                print("User Register Successfully")


    def Login(self):
        User_name = input("Enter  UserName : ")
        Password =  input("Enter Password  : ")
        try:
            with open(User_name + ".txt", 'r') as Data:
                NewData = Data.read()
                NewData = NewData.split('\n')
                self.Name = NewData[0]
                self.User_name = NewData[1]
                self.Password = NewData[2]
                self.Email_id = NewData[3]
                if Password == self.Password:
                    print("User LoggedIn")
                    print(f"Name : {self.Name}")
        except FileNotFoundError:
            print("User not Found")


obj = Auth()

while(True):
    print("Enter 1 for New Register ")
    print("Enter 2 for Login ")
    print("Enter 3 for Exit...! ")
    choice = int(input("Enter your Choice : "))
    match(choice):
        case 1:
            obj.Register()
        case 2:
            obj.Login()
        case 3:
            print("Exiting....!")
            break
        case _:
            print("Invalid Choice")