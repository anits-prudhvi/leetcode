from linked_list import *
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    temp = None
    prev = None
    r_head = None
    counter = 1
    while head!= None:
        if counter%k == 0:
            if r_head == None:
                r_head = ListNode(head.val,None)
                prev = r_head
                head = head.next
            else:
                    prev.next = ListNode(head.val,None)
                    temp = prev.next
                    head = head.next
        else:



head = [1, 2, 3, 4, 5]
k = 2
h = reverseKGroup(convert_list(head),k)