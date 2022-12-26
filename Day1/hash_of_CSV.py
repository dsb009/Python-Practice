if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_c_list = tuple(list(integer_list))
    print (hash(integer_c_list))
    