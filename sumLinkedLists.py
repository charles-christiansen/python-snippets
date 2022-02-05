# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toStr(self):
        v=self
        s=""
        while(v != None):
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
            print("n1 is now "+str(n1))
            e1+=1
            o1=o1.next
        print("===============================")
        n2=0
        e2=0
        o2=l2
        while o2 != None:
            n2+=o2.val * 10**e2
            print("n2 is now "+str(n2))
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

l1=ListNode(2,ListNode(4,ListNode(3,None)))
l2=ListNode(5,ListNode(6,ListNode(4,None)))
s=Solution()
print(s.addTwoNumbers(l1,l2).toStr())
