name=input("Enter name : ")
if name:
    age=input("Enter your age : ")
    age=int(age)
    if age:
        if (name[0]=='A' or name[0]=='a') and age>=10:
            print("You can watch the coco movie !!")
        else:
            print("Sorry Focks!!")
    else:
        print("You didn't write anything !!")
else:
    print("You didn't write anything !!")