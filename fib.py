# 0 1 1 2 3 5 8 13
# Fn = Fn-1 + Fn-2, where n > 1
import time

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

if __name__ == '__main__':
    start = time.time()
    last_index=int(input("Enter the last index for series: "))
    fibo_list = []
    if last_index < 0:
        print("Enter a positive number..!!")
    else:
        for i in range(0,last_index):
            fibo_list.append(fibonacci(i))
    print(fibo_list)
    stop = time.time()
    print(stop-start)






