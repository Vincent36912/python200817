mathgrade=int(input("your math score:"))
engrade=int(input("your english score:"))

if mathgrade>=0 and mathgrade<=100 and engrade>=0 and engrade<=100:
    if mathgrade>=90 and engrade >=90:
        print("give you a gift" )
    elif mathgrade <60 and engrade <60:
        print("loser")
    elif mathgrade<60 or engrade<60:
        print("go go")
else:
    print("error!!!")