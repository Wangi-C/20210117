n = int(input())
num = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())

max_score = -1e9
min_score = 1e9

def dfs(i,now):
    global max_score, min_score, add, sub, mul, div
    if i == n:
        min_score = min(min_score,now)
        max_score = max(max_score,now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1,now + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,now / num[i])
            div += 1
dfs(1,num[0])

print(min_score)
print(max_score)