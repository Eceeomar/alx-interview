#!/usr/bin/python3

def canUnlockAll(boxes):
    """This function defines a function named canUnlockAll
       it takes a list of lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
