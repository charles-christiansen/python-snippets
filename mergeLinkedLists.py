## Add two numbers from linked lists
## LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
## Given 2 linked lists of numbers with digits in ascending order,
## return a linked list that merges the two input lists and
## preserves ascending order.
## Example: if the two input lists were 4->5->6 and 2->2->7,
## the returned list should be 2->2->4->5->6->7

# Definition for singly-linked list.
# __init__ provided by LeetCode with the problem.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toStr(self):
        v=self
        s=""
        while(v != None):
            if len(s)>0:
                s+="->"
            s=s+str(v.val)
            v=v.next
        return s
class Solution:
    def mergeTwoLists(self, list1: ListNode|None, list2: ListNode|None) -> ListNode|None:
        tempHead=ListNode()
        tail=tempHead
        while True:
            if list1 == None:
                tail.next=list2
                break
            elif list2 == None:
                tail.next=list1
                break
            elif list1.val <= list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next

            tail=tail.next
        return tempHead.next

s=Solution()
l1=ListNode(2,ListNode(5,ListNode(6,None)))
l2=ListNode(3,ListNode(4,ListNode(5,None)))
l3=ListNode(0,None)
# return 2->3->4->5->5->6
print(s.mergeTwoLists(l1,l2).toStr())
# return None
print(s.mergeTwoLists(None,None))
# return 0
print(s.mergeTwoLists(l3,None).toStr())
