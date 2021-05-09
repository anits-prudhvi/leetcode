from linked_list import *
def reverselist(head:ListNode,k:int) -> ListNode:
    temp = None
    ptr = head
    r_head = None
    while k:
            temp = ptr.next
            ptr.next = r_head
            r_head = ptr
            ptr = temp
            k -= 1
    return r_head

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


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head
    ptr = head
    counter = 0
    while counter < k and ptr:
        ptr = ptr.next
        counter += 1
    if counter == k:
        rhead = reverselist(head,k)
        head.next = reverseKGroup(ptr,k)
        return rhead
    else:
        return head


head = [1, 2, 3, 4, 5]
k = 2
h = reverseKGroup(convert_list(head),k)
#print_linked_list(reverselist(convert_list(head),2))
print_linked_list(h)
print_linked_list(reverse_list(convert_list(head)))