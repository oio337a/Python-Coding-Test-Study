# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

d = [10_001] * (m + 1)

# dp 테이블
d[0] = 0
for i in range(n):
	for j in range(money[i], m + 1):
		d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10_001:
	print(-1)
else:
	print(d[m])