# ---------------------------------------------------------- #
'''
 ---- example 1 ----
 피보나치 수열 (Fibonacci)
 재귀
'''

def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x - 1) + fibo(x - 2)

# ---------------------------------------------------------- #
'''
 ---- example 2 ----
 피보나치 수열 (Fibonacci)
 재귀, 메모이제이션 적용 
'''

# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수 (top down)
def fibo(x):
	# 종료 조건 (1 or 2 일때 1을 반환)
	if x == 1 or x == 2:
		return 1
	# 이미 계산된 적이 있는 문제라면 그대로 반환
	if d[x] != 0:
		return d[x]
	# 아직 계산하지 않은 문제라면 점화식 계산
	d[x] = fibo(x - 1) + fibo(x - 2)
	return d[x]

# ---------------------------------------------------------- #
'''
 ---- example 3 ----
 피보나치 수열 (Fibonacci)
 반복문, 메모이제이션 사용
'''

# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

d[1], d[2] = 1, 1
n = 99

# 피보나치 함수 반복문 (bottom up)
for i in range(3, n + 1):
	d[i] = d[i - 1] + d[i + 2]

print(d[n])