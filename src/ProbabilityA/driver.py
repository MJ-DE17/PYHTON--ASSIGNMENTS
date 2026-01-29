from util import probability_of_a

n = int(input())
letters = input().split()
k = int(input())

print(f"{probability_of_a(letters, k):.4f}")
