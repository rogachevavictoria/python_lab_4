n = int(input())
arr = []
negative = 0
for i in range(0, n):
    arr.append(int(input()))
    if arr[i] < 0:
        negative = 1
if negative:
    print('Negative number appears.')
else:
    print('Negative number does not appear.')