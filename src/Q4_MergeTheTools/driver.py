from util import merge_the_tools

string = input()
k = int(input())

output = merge_the_tools(string, k)
for line in output:
    print(line)
