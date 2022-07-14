import time 
if __name__ == '__main__':
    time
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
   # for i in range(students):
    #    if students
    print(students)
    print(students.sort(key=score))