from util import process_commands

n = int(input())
commands = [input() for _ in range(n)]

results = process_commands(commands)
for r in results:
    print(r)
