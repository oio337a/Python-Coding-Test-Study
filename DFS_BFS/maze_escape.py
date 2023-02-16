# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''


from collections import deque
# n * m 입력받기
n, m = map(int, input().split())
# n * m 보드 입력받기
board = [list(map(int, input())) for _ in range(n)]
# 큐 생성
que = deque()
que.append((0, 0))  # 시작값 세팅
# 우, 하, 상, 좌
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

while que:
    # 탐색할 좌표 꺼내기
    x, y = que.popleft()
    for i in range(4):
        # 4방 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        # board 벗어나는 경우 무시
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        # 방문하지 않은 곳이면서 갈 수 있는 곳 이면
        if board[nx][ny] == 1:
            # 전 값에 + 1 추가
            board[nx][ny] = board[x][y] + 1
            que.append((nx, ny))  # 다음 탐색할 좌표 추가

# n, m 좌표 출력하기
print(board[n - 1][m - 1])
