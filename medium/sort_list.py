# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        inpoo = []
        
        while head is not None:
            inpoo.append(head.val)
            head = head.next
        

        if len(inpoo) == 0:
            return head

        inpoo.sort(reverse=True)

        out = ListNode(val=inpoo[0])

        for i in range(1, len(inpoo)):
            out = ListNode(val=inpoo[i], next=out)

        return out
