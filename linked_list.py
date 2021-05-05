# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def convert_list(l):
    h = None
    t = None
    for i in l:
        if t == None:
            t = ListNode(int(i),None)
            h = t
        else:
            t.next = ListNode(int(i),None)
            t = t.next
    return h