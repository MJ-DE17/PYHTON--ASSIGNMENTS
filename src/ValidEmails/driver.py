from util import is_valid_email

n = int(input())
emails = [input().strip() for _ in range(n)]

valid = list(filter(is_valid_email, emails))
valid.sort()

print(valid)
