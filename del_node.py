# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def removeElements( head: ListNode, val: int) -> ListNode:
        rh = head
        m = head.next
        pr = head
        while m != None:
            if m.val == val:
                pr.next = m.next
                m.next = None
                if pr.next == None:
                    m = None
                else:
                    m = pr.next
                #pr = pr.next
            else:
                pr = pr.next
                m = m.next
        if rh.val == val:
            return rh.next
        else:
            return rh

print(removeElements(ListNode(1,ListNode(1,ListNode(1,None))),1))