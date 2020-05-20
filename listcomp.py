def listcomp(x,y,z,n):
    ar = []
    p = 0
    for i in range( x+1 ):
        for j in range( y+1 ):
            for k in range( z+1 ):
                if i+j+k != n:
                    ar.append([])
                    ar[p] = [i,j,k]
                    p+=1
    print(ar)

def listcomp2(x,y,z,n):
    v = [[i,j,k] for i in range( x+1 ) for j in range( y+1 ) for k in range( z+1 ) if((i+j+k) != n)]
    print(v)
#list comprehension es como escribir los comandos mas literal
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listcomp(x,y,z,n)
    listcomp2(x,y,z,n)