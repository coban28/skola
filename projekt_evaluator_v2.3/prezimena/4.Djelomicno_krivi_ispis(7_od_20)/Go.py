n = int(input())
L = []
br = []
rj = 0
for i in range(n):
    x = input()
    a, b = map(int,input() .split())
    L += [x]
    be = 0
    while b >= a:
        b = b - a
        b += 2
        be += 1
        rj += 1
    br += [be]
if n % 2 == 0:
    print(rj)
else:
    print(rj - 1)
print(L[br.index(max(br))])
