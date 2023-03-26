#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # create a list to keep track of unlocked boxes
    unlocked[0] = True  # mark the first box as unlocked
    keys = boxes[0]  # get the keys in the first box
    while keys:
        key = keys.pop()  # get the next key from the list
        if not unlocked[key]:  # if the corresponding box is still locked
            unlocked[key] = True  # unlock the box
            keys += boxes[key]  # add the keys in the box to the list
    return all(unlocked)