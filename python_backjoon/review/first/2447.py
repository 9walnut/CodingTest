# 별찍기 10

def star(N):
    if N == 3:
        return ['***', '* *', '***']
    stars = star(N//3)
    arr = []
    for s in stars:
        arr.append(s*3)
    for s in stars:
        arr.append(s+' '*(N//3)+s)
    for s in stars:
        arr.append(s*3)
    return arr


N = int(input())
print(*star(N), sep='\n')
