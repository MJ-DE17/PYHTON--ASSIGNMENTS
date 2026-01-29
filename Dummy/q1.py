if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    total = 0
    count = 0

    for mark in student_marks[query_name]:
        total += mark
        count += 1

    avg = total / count
    print(f"{avg:.2f}")


# python -m unittest test/Q1_StudentAverage/test_student_average.py
