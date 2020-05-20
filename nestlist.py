ar = []

def lala(n,s):
    ar.append([s,n])
def lala2(ar):
    ar.sort()
    v = len(ar)
    print(ar)
    mini = ar[0][0]

    br = [ar[j] for j in range(v) if ar[j][0]!=mini]
    z = len(br)
    min2 = br[0][0]
    #print(br)

    cr = [br[k][1] for k in range(z) if br[k][0]==min2]
    #print(cr)
    for element in cr:
        print(element)


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lala(name,score)
    print(ar)
    lala2(ar)