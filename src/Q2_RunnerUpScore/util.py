def find_runner_up(arr):
    max_score = max(arr)
    runner_up = -10**9

    for x in arr:
        if x != max_score and x > runner_up:
            runner_up = x

    return runner_up