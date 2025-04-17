#!/usr/bin/python3
def canUnlockAll(boxes):
    "prototype of the function"
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = set(boxes[0]) # Get keys from the first box

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
