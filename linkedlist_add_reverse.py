class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        c = 0
        while l1 != None and l2 !=None:
            if res == None:
                t = l1.val + l2.val +c
                c = int(t/10)
                t = int(t%10)
                res = ListNode(t,None)
                res_head = res
            else:
                t = l1.val + l2.val +c
                c = int(t/10)
                t = int(t%10)
                res.next = ListNode(t,None)
                res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            if res == None:
                t = l1.val +c
                c = int(t/10)
                t = int(t%10)
                res = ListNode(t,None)
                res_head = res
            else:
                t = l1.val +c
                c = int(t/10)
                t = int(t%10)
                res.next = ListNode(t,None)
                res = res.next
            l1 = l1.next
        while l2 != None:
            if res == None:
                t = l2.val +c
                c = int(t/10)
                t = int(t%10)
                res = ListNode(t,None)
                res_head = res
            else:
                t = l2.val +c
                c = int(t/10)
                t = int(t%10)
                res.next = ListNode(t,None)
                res = res.next
            l2 = l2.next
        if c!=0:
            res.next = ListNode(c, None)
            res = res.next
        return res_head


l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,None)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,None))))
data = addTwoNumbers(l1,l2)

while data != None:
    print(data.val)
    data = data.next