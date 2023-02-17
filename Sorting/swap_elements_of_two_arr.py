# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''

n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(n):
	if arr_a[i] < arr_b[i]:
		arr_a[i] = arr_b[i]
	k -= 1
	if k == 0:
		break

print(sum(arr_a))

# ---------------------------------------------------------- #
'''
 ---- case 2 ----
'''

n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 우너소를 최대 k번 비교
for i in range(k):
	# A의 원소가 B의 원소보다 작은 경우
	if arr_a[i] < arr_b[i]:
		arr_a[i] = arr_b[i]
	else:
		break

print(sum(arr_a))
