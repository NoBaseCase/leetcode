
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return node
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        else:
            output = ListNode()
            while(temp != None):
                if (l1.val == l2.val):
                    output.val = l1.val
                    output.next = l2
                    output.next.next = 
                    


# def list_size(nodes):
#     count = 0
#     while(nodes != None):
#         count += 1
#         nodes = nodes.next
#     return count


c = ListNode(4, None)
b = ListNode(2, c)
a = ListNode(1, b)

y = ListNode(1, None)
x = ListNode(3, y)
z = ListNode(4, x)

print(list_size(a))
# print(a.next)