def grade_system(mark):
    if(90 <= mark):
        return "A"
    elif(80 <= mark):
        return "B"
    elif(70 <= mark):
        return "C"
    elif(60 <= mark):
        return "D"
    elif(50 <= mark):
        return "E"
    else:
        return "F"
    
math = int(input("Enter mark for Math : "))
english = int(input("Enter mark for english : "))
hindi = int(input("Enter mark for hindi : "))

print("  Subject      Mark   Grade")
print(f" Math     -->  {math} --  {grade_system(math)}")
print(f" English  -->  {english} --  {grade_system(english)}")
print(f" Hindi    -->  {hindi} --  {grade_system(hindi)}")