#!/usr/bin/python3
"""This module defines a function to check if all boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): Each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = set(boxes[0])  # Get keys from the first box

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
