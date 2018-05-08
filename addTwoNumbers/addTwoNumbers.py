#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

class ListNode(self,x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        numbers=[0,0]
        for i in range(2):
            idx = 0
            if i == 0:
                node = l1
            else:
                node = l2
            while node:
                numbers[i] += node.val*pow(10,idx)
                node = node.next
                idx += 1
        twoSum = numbers[0] + numbers[1]

        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for item in str(twoSum)[::-1]:
            ptr.next = ListNode(int(item))
            ptr = ptr.next
        ptr = dummyRoot.next
        return ptr


            
