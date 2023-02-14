# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''
from collections import deque

n, m = map(int, input().split())

x, y, d = map(int, input().split())
board = [input().split() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque((x, y))
cnt = 1 if int(board[x][y]) == 0 else 0
while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n + 1 and 0 <= ny and ny < m + 1:
            if int(board[nx][ny]) == 0:
                board[nx][ny] = 1
                cnt += 1
                que.append((nx, ny))
print(cnt)