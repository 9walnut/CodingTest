# 별찍기 10

N = int(input())


def star(N):
    if N == 3:
        return ["***", "* *", "***"]
    stars = star(N//3)
    arr = []
    for s in stars:
        arr.append(s*3)
    for s in stars:
        arr.append(s + ' '*(N//3) + s)
    for s in stars:
        arr.append(s*3)
    return arr


print(*star(N), sep='\n')
