#감시 피하기#3
from itertools import combinations
n = int(input())
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(list(map(input().split())))
    for j in range(n):
        if board[i][j] == "X":
            spaces.append((i,j))
        elif board[i][j] == "T":
            teachers.append((i,j))

def watch(x,y,direction):
    if direction == 0:
        while x >= 0:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x -= 1
    if direction == 1:
        while x < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x += 1
    if direction == 2:
        while y >= 0:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            y -= 1
    if direction == 3:
        while y < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            y += 1

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find = False

for data in combinations(spaces,3):
    for x,y in data:
        board[x][y] = "O"
    if not process():
        find = True
        break
    for x,y in data:
        board[x][y] = "X"

if find == True:
    print("yes")
else:
    print("no")