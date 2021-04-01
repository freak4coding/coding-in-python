pos=int(input("Enter position upto which you want to print : "))
def fibo_series(x):
    a=[]
    if x==1:
       a.append(0)
    elif x<=0:
        print("Invalid input !!")
    else:
        a.append(0)
        a.append(1)
        for i in range(2,x):
            a.append(int(a[i-1])+int(a[i-2]))
    return a
print(fibo_series(pos))