#감시 피하기 #2

from itertools import combinations
n = int(input())
data = []
teachers = []
spaces = []
for i in range(n):
    data.append(list(map(input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == "X":
            spaces.append((i,j))
        elif data[i][j] == "T":
            teachers.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def watch(x,y,direction):
    if direction == 0:
        while x >= 0:
            if data[x][y] == "S":
                return True
            elif data[x][y] == "O":
                return False
            x -= 1
    if direction == 1:
        while x < n:
            if data[x][y] == "S":
                return True
            elif data[x][y] == "O":
                return False
            x += 1
    if direction == 2:
        while y >= 0:
            if data[x][y] == "S":
                return True
            elif data[x][y] == "O":
                return False
            y -= 1
    if direction == 3:
        while y < 0:
            if data[x][y] == "S":
                return True
            elif data[x][y] == "O":
                return False
            y += 1

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find = False

for d in combinations(spaces,3):
    for x,y in d:
        data[x][y] = "O"
    if not process():
        find = True
        break
    for x,y in d:
        data[x][y] = "X"

if find:
    print("yes")
else:
    print("no")