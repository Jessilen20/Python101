def run(n,lis):
    b = list(lis)
    b.sort()
    b.reverse()
    a = b[0]
    v = b.count(a)
    for j in range(0,v):
        b.remove(a)
        print(b)
    print(b[0])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run(n,arr)