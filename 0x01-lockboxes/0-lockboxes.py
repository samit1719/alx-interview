#!/usr/bin/python3
"""
************
"""


def canUnlockAll(boxes):
    """
    Check if opend or not
    """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True