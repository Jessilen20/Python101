import math

def cont(n):
    y=0
    for i in range(1,n+1):
       digito= int(math.log10(i)) + 1
       y= y*(10**digito) + i
           
    return print(y)

if __name__ == '__main__':
    n = int(input())
    cont(n)