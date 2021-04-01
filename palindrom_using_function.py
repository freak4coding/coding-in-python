def is_palindrom(x):
    return x==x[::-1]
string=input("Enter a string : ")
print(is_palindrom(string))