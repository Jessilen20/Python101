fr =[]

def funciones(n):
    for k in range(n):
        fr.append(input().split())
    print(fr)
    list1 = []

    for j in range(n):
        if fr[j][0] == "insert":
            i = int(fr[j][1])
            e = int(fr[j][2])
            list1.insert(i,e)

        if fr[j][0] == "print":
            print(list1)

        if fr[j][0] == "remove":
            e = int(fr[j][1])
            list1.remove(e)

        if fr[j][0] == "append":
            e = int(fr[j][1])
            list1.append(e)

        if fr[j][0] == "sort":
            list1.sort()

        if fr[j][0] == "pop":
            list1.pop()

        if fr[j][0] == "reverse":
            list1.reverse()

      

if __name__ == '__main__':
    N = int(input())
    funciones(N)
