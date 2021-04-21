class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def isPalindrome(head: ListNode) -> bool:
        stack = []
        t = head
        while t != None:
            stack.append(t.val)
            t = t.next
        t = head
        while t != None:
            if t.val != stack.pop():
                return False
            t = t.next
        if len(stack) != 0:
            return False
        return True

def isPalin(self,head: ListNode) -> bool:
        fh = head
        def check_rec(temp_head: ListNode) -> bool:
            if temp_head != None:
                if not check_rec(temp_head.next):
                    return False
                if self.fh.val != temp_head.val:
                    return False
                fh = self.fh.next
            return True
h = ListNode(1,ListNode(2,ListNode(2)))

print(isPalindrome(h))