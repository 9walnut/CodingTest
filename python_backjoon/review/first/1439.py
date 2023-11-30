# 뒤집기
S = input()
count = 0
# -1 해주는 이유는 i+1로 검색하기 때문에 그 이후는 조건에서 벗어나기 때문
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count+1)//2)
