from collections import namedtuple

def average_marks(n, fields, rows):
    Student = namedtuple('Student', fields)
    total = 0

    for row in rows:
        total += int(Student(*row).MARKS)

    return round(total / n, 2)
