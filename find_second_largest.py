#!/usr/local/bin/python3

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def findLargest(root):
    travel = root
    while travel.right is not None:
        if travel.right.right is not None:
            travel = travel.right.right
        else:
            break
        travel = root.right
    # travel is the largest
    return travel
    
def findSecondLargest(root):
    traverse = root
    cache = None
    while traverse:
        if traverse.right is None:
            if traverse.left is not None:
                return findLargest(traverse.left)
            else:
                return traverse
        else:
            cache = traverse
        traverse = traverse.right
        if traverse.right is None:
            break
    return cache

if __name__ == '__main__':
    first = BinaryTreeNode(6)
    second = first.insert_left(4)
    third = first.insert_right(10)
    fourth = second.insert_right(5)
    fifth = second.insert_left(3)
    sixth = third.insert_left(7)
    seventh = third.insert_right(12)
    print(findSecondLargest(first).value)
