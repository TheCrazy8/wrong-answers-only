import random

questions = []

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

def main():
    addq()
    addqlist1()
    
if __name__ == '__main__':
    main()
