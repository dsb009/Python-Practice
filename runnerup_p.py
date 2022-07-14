if __name__ == '__main__':
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)] 

    maxi = [ x for x in arr if x < max(arr)]
    y = max(maxi)
    print (y)