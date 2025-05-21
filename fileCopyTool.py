def CopyTool(oldFileName, newFileName):
    try:
        Datas = ''
        with open(oldFileName, 'r') as oldFile:
            Datas = oldFile.read()
        with open(newFileName, 'w') as newFile:
            newFile.write(Datas)
            print("New File Created Successfully")
    except FileNotFoundError:
        print(f"{oldFileName} is Not Found")
        

CopyTool(input("Enter Old File Name|Path : "), input("Enter New File Name|Path : "))