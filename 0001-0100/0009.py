import math
n = int(input())
numbers = list(map(int, input().split( )))
max_ind, min_ind = numbers.index(max(numbers)), numbers.index(min(numbers))
mult = 1
for i in range(min_ind + int(math.copysign(1, max_ind - min_ind)), max_ind, int(math.copysign(1, max_ind - min_ind))):
    mult *= numbers[i]
print(sum(x for x in numbers if x > 0), mult)