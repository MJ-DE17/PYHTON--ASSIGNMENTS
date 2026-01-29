from util import word_order

n = int(input())
words = [input().strip() for _ in range(n)]

result = word_order(words)
print(len(result))
print(*result.values())
