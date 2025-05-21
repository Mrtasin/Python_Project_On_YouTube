from string import punctuation as spl

def PasswordChecker(Password) :
    temp = 0
    if(len(Password) >= 8):
        temp += 1
    else:
        print("Password is too short. It should be at least 8 characters long.")

    if(any(chr.isdigit()  for chr in Password)):
        temp += 1
    else:
        print("Password should contain at least one digit.")

    if(any(chr.islower()  for chr in Password)):
        temp += 1
    else:
        print("Password should contain at least one lowercase letter.")

    if(any(chr.isupper()  for chr in Password)):
        temp += 1
    else:
        print("Password should contain at least one uppercase letter.")

    if(any(((chr in spl) for chr in Password))):
        temp += 1
    else:
        print("Password should contain at least one special character.")

    if temp >= 5:
        return "Storng"
    elif temp >= 3:
        return "Medium"
    else:
        return "Week"



password = input("Enter Password : ")
data = PasswordChecker(password)

print("Password :",data)