# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''
n, m = map(int, input().split())

card = [map(int, input().split()) for _ in range(n)]

result = 0

for i in range(n):
    if (min(card[i]) > result):
        result = min(card[i])

print(result)


# ---------------------------------------------------------- #
'''
 ---- case 2 ----
'''

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    
    min_value = min(data)
    
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)