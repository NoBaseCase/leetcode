from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # temporary node to start new list
    output = ListNode(None)
    # keeps track of the current place in the new list
    current = output
    # if l1 and l2 exist:
    while l1 and l2:
        # sets new list to point to l1, then l1 moves to the next node on the right
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        # update the position of current in preparation for the next node
        current = current.next
    # if only one list left, point the next field of the node to that list
    if l1:
        current.next = l1
    else:
        current.next = l2

    # Since the output starts with None value, we must return the next node, if it exists
    return output.next


class Solution:
    pass


c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

y = ListNode(1, None)
x = ListNode(3, y)
z = ListNode(4, x)

test = Solution()
print(merge_two_lists(a, z))
