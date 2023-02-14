# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

position = input()
row = int(position[1])
col = int(ord(position[0])) - int(ord('a')) + 1  # ord 아스키 코드를 숫자로 변환하는 함수

cnt = 0
# 이동 할 수 있는 8가지 방향 정의
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(8):
	# 다음 이동위치로 이동
	nx = row + dx[i]
	ny = col + dy[i]
	# 이동 가능 하면 cnt 증가
	if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
		cnt += 1

print(cnt)