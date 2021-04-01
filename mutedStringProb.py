if __name__ == '__main__':
    n=int(input())
    student=[[0 for j in range(2)] for i in range(n)]
    for i in range(n):
        student[i][0]=input()
        student[i][1]=float(input())
    m=[mark for [name,mark] in student]
    m.remove(min(m))
    name = [name for [name,mark] in student if mark == min(m)]
    name.sort()
    for n in name:
        print(n)
