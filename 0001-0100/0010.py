coeff = list(map(int, input().split( )))
a,b,c,d = coeff[0],coeff[1],coeff[2],coeff[3]
roots = []
for i in range(-100, 101):
    if a * i ** 3 + b * i ** 2 + i * c + d == 0:
        roots.append(i)
print(*roots)