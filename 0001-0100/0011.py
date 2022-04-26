def count(k, n):
    s = 0
    if n < 0:
        return 0
    if n <= 1:
        return 1
    for i in range(1, k + 1):
        s += count(k, n - i)
    return s
    

k, n = list(map(int, input().split()))
print(count(k, n))