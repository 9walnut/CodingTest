#  잃어버린 괄호
s = input().split('-')

sum = 0
# -를 만나기 전 의 0번 인덱스내의 숫자를 더하기
for i in s[0].split('+'):
    sum += int(i)

# 0번재 이후 원소 더해주기
for i in s[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
