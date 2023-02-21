# ---------------------------------------------------------- #
'''
 ---- case 1 ----
 이진 탐색 (재귀)
'''

def binary_search(arr, num, s, e):
	mid = (s + e) // 2
	if s > e:
		return None
	if (arr[mid] == num):
		return mid
	elif (arr[mid] > num):
		return binary_search(arr, num, s, mid - 1)
	else:
		return binary_search(arr, num, mid + 1, e)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

arr.sort()
for i in find:
	result = binary_search(arr, i, 0, n - 1)
	if (result != None):
		print("yes", end=" ")
	else:
		print("no", end=" ")

# ---------------------------------------------------------- #
'''
 ---- case 2 ----
 카운트 정렬
'''

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

arr.sort()
count_sort = [0] * arr[-1]
for i in arr:
	count_sort[i - 1] += 1
for check in find:
	if count_sort[check -1] != 0:
		print("yes", end=" ")
	else:
		print("no", end=" ")

# ---------------------------------------------------------- #
'''
 ---- case 3 ----
 집합 자료형 사용
'''

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
find = list(map(int, input().split()))

for i in find:
	if i in arr:
		print("yes", end=" ")
	else:
		print("no", end=" ")