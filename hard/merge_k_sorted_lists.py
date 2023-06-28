# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fred = []
        
        for i in lists:
            x = i
            while x is not None:
                fred.append(x.val)
                x = x.next

        out = ListNode()

        if len(fred) == 0:
            return None
        fred.sort()

        for i in reversed(range(len(fred))):

            if i == len(fred)-1:
                out.val = fred[i]
            else:
                out = ListNode(fred[i], out)
        
        return out
