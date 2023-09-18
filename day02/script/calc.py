import math

res = (1 + 11+111+1111+11111+111111+1111111+11111111+111111111)

def nombre(n):
    return ['1' *k for k in range(1, n+1)]

i_nombre = int(9)

for x in nombre(i_nombre):
  print(f'{x} + {(x)} = {int(x) + int(x)**2}')

print(res, res**2, res**3, res**4, res**5, res**6, res**7)

a = 10 **1024
print (a)