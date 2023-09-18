pi = 0
a = 1
for i in range(10, 1000000, 2):
    pi += (4/i) * a
    a *= -1
    print(pi)

