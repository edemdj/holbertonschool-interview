def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # On commence par la première boîte (toujours ouverte)
    keys = set(boxes[0])  # On prend les clés dans la boîte 0

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
