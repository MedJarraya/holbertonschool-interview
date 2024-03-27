#!/usr/bin/python3
"""
This method determines if all the boxes can be opened!
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    keys = set([0])
    opened = set()

    while keys:
        box_index = keys.pop()
        opened.add(box_index)
        box = boxes[box_index]
        for key in box:
            if key not in opened and key < len(boxes):
                keys.add(key)

    return len(opened) == len(boxes)
