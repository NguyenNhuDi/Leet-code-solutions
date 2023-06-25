# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,ll):
        prev = None
        current = ll

        while True:
            next_node = current.next
            current.next = prev
            prev = ListNode(current.val,current.next)
            try:
                current = ListNode(next_node.val,next_node.next)
            except:
                break
        return prev



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        out = ListNode()
        first = True
        remainder = 0
        
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + remainder
            if first:
                out.val = (val % 10)    
                first = False
            else:
                out = ListNode(val % 10, out)

            remainder = val // 10

            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            val = l1.val + remainder
            out = ListNode(val % 10, out)
            remainder = val // 10
            l1 = l1.next       
        
        while l2 is not None:
            val = l2.val + remainder
            out = ListNode(val % 10, out)
            remainder = val // 10
            l2 = l2.next
        

        if remainder > 0:
            out = ListNode(remainder,out)


        return self.reverse(out)
