# ---------------------------------------------------------- #
'''
 ---- case 1 ----
 기본 정렬 방법
'''

n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

for i in arr:
	print(i, end=' ')

# ---------------------------------------------------------- #
'''
 ---- case 1 ----
 키 값으로 정렬하는 방법
'''

n = int(input())

arr = []

for i in range(n):
	input_data = input().split()
	arr.append((input_data[0], int(input_data[1])))

arr.sort(key=lambda score: score[1])

for student in arr:
	print(student[0], end=' ')
