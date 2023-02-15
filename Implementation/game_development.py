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

que = deque()
que.append((x, y))
cnt = 0
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

# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x좌표, y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북동남서 입력받기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_left = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][dy] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_left = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_left += 1
        # 네방향 모두 갈 수 없는 경우
        if turn_left == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if arr[nx][ny] == 0:
                x, y = nx, ny
                # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_left = 0

# 정답 출력
print(count)
