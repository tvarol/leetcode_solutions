#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Beats 40% of python solutions
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        while l1 and l2:
            if l2.val >= l1.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
        
        if l1:
            node.next = l1
        
        if l2: 
            node.next = l2
    
        return dummy.next

#ALTERNATIVE SOLUTION, BEATS 98% of python submissions:
"""
def mergeTwoLists(self, l1, l2):
        l0 = ListNode(None)
        l = l0
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l.next = l1
            l = l.next
            l1 = l1.next
        l1 = l1 or l2
        l.next = l1
        return l0.next
"""
