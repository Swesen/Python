a = [64, 34, 25, 12, 22, 11, 13, 90]
d = 20
n = len(a)

# sort a smallest to largest
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

# print every number in a that is larger than d except the last
for i in range(n - 1):
    if a[i] >= d:
        print("%d" % a[i])
