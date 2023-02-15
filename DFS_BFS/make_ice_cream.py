# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n, m = map(int, input().split())
# 2차원 리스트 맵 입력 받기
graph = [list(map(int, input())) for _ in range(n)]

# DFS로 특정한 노드를 방문한 뒤에 연결되 ㄴ모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나면 재귀 탈출
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문 체크
        # 상, 좌, 하, 우 체크
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False


count = 0

for x in range(n):
    for y in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(x, y) == True:
            count += 1
print(count)
