from linked_list import *
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        r = None
        main_head = None
        c = 0
        while l1 != None and l2 != None:
            t1 = int(l1.val) + int(l2.val)
            temp = (t1 + c)%10
            c = (t1 + c) /10
            if r == None:
                r = ListNode(temp,None)
                main_head = r
            else:
                r.next = ListNode(temp,None)
                r = r.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            r.next = ListNode((int(l1.val)+c)%10,None)
            r = r.next
            c = int((l1.val + c) / 10)
            l1 = l1.next
        while l2 != None:
            r.next = ListNode((int(l2.val)+c)%10,None)
            r = r.next
            c = int((l2.val + c) / 10)
            l2 = l2.next
        if c != 0:
            r.next = ListNode(int(c),None)
        return main_head

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
h = addTwoNumbers(convert_list(l1),convert_list(l2))
while h != None:
    print(h.val)
    h = h.next



