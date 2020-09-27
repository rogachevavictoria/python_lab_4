c = 0
for i in range(10, 100):
    if (i / 10) > (i % 10):
        print(i)
        c += i
print('sum =', c)
