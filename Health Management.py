print("Welcome to Health Management System\n")
def hab():
    h=int(input("1 for exercise and 2 for food: "))
    return h
def cname():
    name=int(input("Enter 1 for Harry, 2 for Rohan, 3 for Hammad:"))
    return name
def value():
    v=int(input("1 for logging the value, 2 for retrieving the value: "))
    return v
import datetime
def gettime():
    return datetime.datetime.now()


def take(name):
    if name==1:
        h=hab()
        v=value()
        if v==1:
            if h==1:
                with open("harryex.txt","a") as fh:
                    ex=input("Enter the exe1rcise\n")
                    fh.write(str(gettime())+":"+ex+"\n")
            elif h==2:
                with open("harryfd.txt","a") as fh:
                    fd=input("Enter the food\n")
                    fh.write(str(gettime())+":"+fd+"\n")
            print("Successfully locked the value")
        elif v==2:
            if h==1:
                 with open("harryex.txt") as fh:
                     for i in fh:
                         print(i,end="")
            elif h==2:
                with open("harryfd.txt") as fh:
                    for i in fh:
                         print(i,end="")
    elif name==2:
        h=hab()
        v=value()
        if v==1:
            if h==1:
                with open("rohanex.txt","a") as fh:
                    ex=input("Enter the exercise\n")
                    fh.write(str(gettime())+":"+ex+"\n")
                    fh.write("\n")
            elif h==2:
                with open("rohanfd.txt","a") as fh:
                    fd=input("Enter the food\n")
                    fh.write(str(gettime())+":"+fd+"\n")
            print("Successfully locked the value")
        elif v==2:
            if h==1:
                 with open("rohanex.txt") as fh:
                    for i in fh:
                         print(i,end="")
            elif h==2:
                with open("rohanfd.txt") as fh:
                    for i in fh:
                         print(i,end="")
    elif name==3:
        h=hab()
        v=value()
        if v==1:
            if h==1:
                with open("hammadex.txt","a") as fh:
                    ex=input("Enter the exercise\n")
                    fh.write(str(gettime())+":"+ex+"\n")
            elif h==2:
                with open("hammadfd.txt","a") as fh:
                    fd=input("Enter the food\n")
                    fh.write(str(gettime())+":"+fd+"\n")
            print("Successfully locked the value")
        elif v==2:
            if h==1:
                 with open("hammadex.txt") as fh:
                    for i in fh:
                         print(i,end="")
            elif h==2:
                with open("hammadfd.txt") as fh:
                    for i in fh:
                         print(i,end="")
            

                    
nm=cname()
take(nm)
                   
