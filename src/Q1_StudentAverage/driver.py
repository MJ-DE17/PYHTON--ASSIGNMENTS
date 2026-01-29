from util import calculate_average

n = int(input())
student_marks = {}

for _ in range(n):
    name , *line = input().split()
    scores = list(map(float ,line))
    student_marks[name] = scores

query_name = input()

avg = calculate_average(student_marks[query_name])
print(f"{avg :.2f}")