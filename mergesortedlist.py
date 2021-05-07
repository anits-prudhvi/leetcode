from linked_list import *
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        temp =None
        Head = None
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                if temp == None:
                    temp = ListNode(l2.val,None)
                    Head = temp
                else:
                    temp.next = ListNode(l2.val,None)
                    temp = temp.next
                l2 = l2.next
            elif l1.val <= l2.val:
                if temp == None:
                    temp = ListNode(l1.val, None)
                    Head = temp
                else:
                    temp.next = ListNode(l1.val, None)
                    temp = temp.next
                l1 = l1.next
        while l1 != None:
            if temp:
                temp.next = ListNode(l1.val,None)
                temp = temp.next
            else:
                temp = ListNode(l1.val,None)
                Head = temp
            l1 = l1.next
        while l2 != None:
            if temp:
                temp.next = ListNode(l2.val,None)
                temp = temp.next
            else:
                temp = ListNode(l2.val,None)
                Head = temp
            l2 = l2.next
        return Head

def MergeSortedlists(l1:ListNode,l2:ListNode)->ListNode:
        temp = None
        Head = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                if Head == None:
                    temp = l1
                    Head = temp
                    l1 = l1.next
                    temp.next = None
                else:
                    temp.next = l1
                    l1 = l1.next
                    temp = temp.next
                    temp.next = None
            else:
                if Head == None:
                    temp = l2
                    Head = temp
                    l2 = l2.next
                    temp.next = None
                else:
                    temp.next = l2
                    l2 = l2.next
                    temp = temp.next
                    temp.next = None

        if l1 != None:
            temp.next = l1
            return Head
        if l2 != None:
            temp.next = l2
            return Head

l1 = [1,2]
l2 = [0,4]
h = mergeTwoLists(convert_list(l1),convert_list(l2))
while h != None:
    print(h.val)
    h = h.next
h = MergeSortedlists(convert_list(l1),convert_list(l2))
while h != None:
    print(h.val)
    h = h.next