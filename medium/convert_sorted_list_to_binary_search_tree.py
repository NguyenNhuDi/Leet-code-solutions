# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def addNode(self, head, x):
        if head is None:
            return x

        # Node is to the right
        if x.val >= head.val:
            head.right = self.addNode(head.right, x)
        # Node is to the left
        else:
           head.left =  self.addNode(head.left, x)

        return head

    def binaryAdd(self,l, r, head, arr):
        if l >= r:
            return

        m = (l + r) // 2

        head = self.addNode(head, TreeNode(arr[m]))

        # Add to the left
        self.binaryAdd(l, m, head, arr)

        # Add to the right
        self.binaryAdd(m + 1, r, head, arr)

        return head

    def sortedListToBST(self, head):
        sorted_arr = []

        h = head

        if h is None:
            return None

        while h is not None:
            sorted_arr.append(h.val)
            h = h.next
            

        m = len(sorted_arr) // 2

        h = TreeNode(sorted_arr[m])

        self.binaryAdd(0, m, h, sorted_arr)
        self.binaryAdd(m+1,len(sorted_arr), h, sorted_arr)

        return h
