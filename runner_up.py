def runnerup(arr):
    sublist=[x for x in arr if x < max(arr)]
    return max(sublist)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(runnerup(arr))
   
   
            