# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n = int(input())

# dp 테이블 생성
d = [0] * 30_001

# dp (bottom up)
for i in range(2, n + 1):
	# 현재 수에서 1을 빼는 경우
	d[i] = d[i - 1] + 1
	# 현재 수가 2로 나누어 지는 경우
	if i % 2 == 0:
		d[i] = min(d[i], d[i // 2] + 1)
	# 현재 수가 2 나누어 지는 경우
	if i % 3 == 0:
		d[i] = min(d[i], d[i // 3] + 1)
	# 현재 수가 2로 나누어 지는 경우
	if i % 5 == 0:
		d[i] = min(d[i], d[i // 5] + 1)

print(d[n])