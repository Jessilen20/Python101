def tupl(m):
    n = tuple(m)
    print(n)
    print(hash(n))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupl(integer_list)