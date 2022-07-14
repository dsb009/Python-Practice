if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    maxi = [ x for x in arr if x < max(arr)]
    print (maxi)
    y = max(maxi)
    print (y)