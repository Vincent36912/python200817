grade=float(input("your score:"))

if grade >=0 and grade<=100:
    if grade>=90:
        print("level A")
    elif grade>=80:
        print("level B")
    elif grade>=70:
        print("level C")
    elif grade>=60:
        print("level D")
    else:
        print("level E")
    
else:
    print("error!!!")
