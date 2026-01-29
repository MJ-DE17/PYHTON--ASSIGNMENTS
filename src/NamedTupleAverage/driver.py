from util import average_marks

n = int(input())
fields = input().split()
rows = [input().split() for _ in range(n)]

print(f"{average_marks(n, fields, rows):.2f}")
