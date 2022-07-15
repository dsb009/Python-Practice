import time 
if __name__ == '__main__':
    start_time= time.time()
    students=[]
    # students=[['Rachel',-50], ['Mawer',-50], ['Sheen',-50],['Shaheen',51]]
    for _ in range(int(input("Enter range: "))):
       students.append([input("Enter name of student: "),float(input("Enter the marks of the student: "))])
        
    #second_lowest = sorted(students)[1][1]#this does not hadle duplicate values as marks 
    second_lowest = sorted(list(set([marks for name,marks in students])))[1]
    # print(sorted(students))
    #print(second_lowest)
    print('\n'.join([a for a,b in sorted(students) if b == second_lowest]))
    end_time= time.time()
    print("Time taken is: {}".format( start_time - end_time)) 

    