def wordCounter(fileName):
    try:
        with open(fileName,'r') as fileOpen:
            CounterWord = 0
            for dataItems in fileOpen:
                words = dataItems.split()
                CounterWord += len(words)
            else:
                return CounterWord
    except FileNotFoundError:
        print("File Not Found")
        
    return None
    
words = wordCounter(input("Enter File full path : "))

if(words != None):
    print("Words : ",words)