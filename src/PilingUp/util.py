from collections import deque

def can_stack(blocks):
    blocks = deque(blocks)
    last = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            pick = blocks.popleft()
        else:
            pick = blocks.pop()

        if pick <= last:
            last = pick
        else:
            return False

    return True
