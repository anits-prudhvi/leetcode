# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def convert_list(l:list)->ListNode:
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

def reverse_list(head:ListNode)->ListNode:
    r_head = None
    temp = None
    ptr = head
    while ptr:
        temp = ptr.next
        ptr.next = r_head
        r_head = ptr
        ptr = temp
    return r_head

def print_linked_list(head:ListNode):
    while head:
        print(head.val)
        head = head.next