n = int(input())
marks = list(map(int, input().split()))
marks_3 = []
marks_4 = []
for i in marks:
    if i % 2 == 0:
        marks_4.append(i)
    else:
        marks_3.append(i)
print(*marks_3)
print(*marks_4)
if len(marks_4) >= len(marks_3):
    print("YES")
else:
    print("NO")
