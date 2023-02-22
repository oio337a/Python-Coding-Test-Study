# ---------------------------------------------------------- #
'''
 ---- case 1 ----
 순차 탐색 (시간 초과 날 가능성 많음)
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

# ---------------------------------------------------------- #
'''
 ---- case 2 ----
 이진 탐색
'''

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start  = 0
end = (max(rice_cake))

# 이진 탐색 수행 (반복)
result = 0
while (start <= end):
	total = 0
	mid = (start + end) // 2
	for x in rice_cake:
		# 잘랐을 때의 떡의 양 계산
		if x > mid:
			total += x - mid
	# 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
	if total < m:
		end = mid - 1
	else:
		result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
		start = mid + 1
print(result)
