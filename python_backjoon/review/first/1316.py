n = int(input())
cnt = n

for _ in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        # 위의 경우가 아닌 경우에서 같은 글자가 나온 경우
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
