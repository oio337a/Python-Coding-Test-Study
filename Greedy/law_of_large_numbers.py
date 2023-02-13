# ---------------------------------------------------------- #
'''
 ---- case 1 ----
'''
list_size, cnt, repeat_cnt = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

max = data[-1]
sec_num = data[-2]

result = 0

while 1:
    for i in range(repeat_cnt):
        if (cnt == 0):
            break
        result += max
        cnt -= 1
    if cnt == 0:
        break
    result += sec_num
    cnt -= 1

print(result)


# ---------------------------------------------------------- #
'''
 ---- case 2 ----
'''
list_size, cnt, repeat_cnt = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

max = data[-1]
sec_num = data[-2]

result = 0

count = (cnt // (repeat_cnt + 1)) * repeat_cnt
count += cnt % (repeat_cnt + 1)

result += count * max
result += (cnt - count) * sec_num