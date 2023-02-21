# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort(reverse=True)

cut_size = rice_cake[0] - 1
result = 0
while(cut_size >= 0):
	for i in rice_cake:
		if i < cut_size:
			break
		result += abs(cut_size - i)
	if result >= m:
		print(cut_size)
		break
	result = 0
	cut_size -= 1