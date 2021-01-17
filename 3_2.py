#경쟁적 전염#3
from collections import deque

n, k = map(int,input().split())
virus = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j],0,i,j))

virus.sort()
queue = deque(virus)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

target_s, target_x, target_y = map(int,input().split())

while queue:
    v,s,x,y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append((v,s+1,nx,ny))

print(graph[target_x-1][target_y-1])