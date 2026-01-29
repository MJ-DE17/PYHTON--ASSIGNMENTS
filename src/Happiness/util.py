def calculate_happiness(arr, A, B):
    happiness = 0
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
    return happiness
