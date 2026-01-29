from util import find_runner_up

n = int(input())
arr = list(map(int, input().split()))

result = find_runner_up(arr)
print(result)