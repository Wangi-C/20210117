n, m = map(int,input().split())
data = [[0]*m for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                virus(nx,ny)

def getscore():
    score = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                score += 1
    return score

result = 0
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                data[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2:
                    virus(i,j)
        result = max(result,getscore())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)