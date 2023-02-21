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

