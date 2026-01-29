from itertools import combinations

def probability_of_a(letters, k):
    n = len(letters)
    total = 0
    favorable = 0

    for combo in combinations(range(n), k):
        total += 1
        if any(letters[i] == 'a' for i in combo):
            favorable += 1

    return round(favorable / total, 4)
