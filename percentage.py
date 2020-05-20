import decimal

def promedio(dic,elegido):
    print(dic)
    m = dic[elegido]
    prom = (m[0]+ m[1] + m[2])/3
    print('{0:.2f}'.format(prom))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    promedio(student_marks,query_name)