import random

questions = []
qlist1 = ["What's your superhero name?",
"What is the most embarrassing thing that has happened to you?",
"If you could have any superpower, what would it be?",
"If you could teleport to any location, where would you go?",
"What would your superhero costume look like?",
"Would you rather live a normal life or a weird life?",
"What's the spiciest food you've ever eaten?",]

qlist2 = ["What does the word \"Desert\" translate as from Latin?",
"How many weeks before Christmas does the 2003 film \"Love Actually\" begin?",
"what is 1+1?",
"how much wood could a wood chuck chuck if a wood chuck could chuck wood?",
"how old is Benjamin Green?",
""]

def addq():
    q = input("What question would you like to add? ")
    questions.append(q)
    qadloop()
    
def qadloop():
    if input("Add another? ") == "y":
        addq()
    else:
        pass

def askq():
    pass

def addqlist1():
    if input("do you want to add default question list 1? ") == "y"
    questions.append(qlist1)

def addqlist2():
    if input("do you want to add default question list 2? ") == "y"
    questions.append(qlist2)

def ans():
    n = len(questions)
    a = random.randint(1,n)
    quans = questions[a]
    del questions[a]
    print(quans)
    if input("continue? ") == "y":
        pass
    else:
        print("done")
        return("done")
    if n == 0:
        print("none left")
        return("none left")
    else:
        ans()

def main():
    addq()
    addqlist1()
    ans()

if __name__ == '__main__':
    main()
