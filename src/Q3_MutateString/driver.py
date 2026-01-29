from util import mutate_string

s = input()
i, c = input().split()

result = mutate_string(s, int(i), c)
print(result)
