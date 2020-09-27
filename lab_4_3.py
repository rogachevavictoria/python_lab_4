from numpy import arange

m = []
minimal = 9999
print(' x  | f(x) ')
for x in arange(0.0, 1.0, 0.1):
    print(round(x, 2), '|', round(15 * pow(x, 2) + 10 * x - 1, 2))
    if round(15 * pow(x, 2) + 10 * x - 1, 2) < minimal:
        minimal = round(15 * pow(x, 2) + 10 * x - 1, 2)
        m.append(x)
print('function is minimal when x =', m.pop())