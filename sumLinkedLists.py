## Add two numbers from linked lists
## LeetCode: https://leetcode.com/problems/add-two-numbers/
## Given 2 linked lists of numbers with digits in reverse order,
## return a linked list containing the sum of the two numbers
## in the same format.
## Example: if the two input lists were 4->5->6 and 2->2->7,
## the returned list should be 6->7->3->1

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=0
        e1=0
        o1=l1
        while o1 != None:
            n1+=o1.val * 10**e1
            e1+=1
            o1=o1.next
        n2=0
        e2=0
        o2=l2
        while o2 != None:
            n2+=o2.val * 10**e2
            e2+=1
            o2=o2.next
        sum=n1+n2
        unlinked=[int(digit) for digit in str(sum)]
        nnode=None
        pln=ListNode()
        for lnval in unlinked:
            ln=ListNode(lnval,nnode)
            nnode=ln
        return ln

s=Solution()
l1=ListNode(2,ListNode(4,ListNode(3,None)))
l2=ListNode(5,ListNode(6,ListNode(4,None)))
print(s.addTwoNumbers(l1,l2).toStr())

l3=ListNode(4,ListNode(5,ListNode(6,None)))
l4=ListNode(2,ListNode(2,ListNode(7,None)))
print(s.addTwoNumbers(l3,l4).toStr())
