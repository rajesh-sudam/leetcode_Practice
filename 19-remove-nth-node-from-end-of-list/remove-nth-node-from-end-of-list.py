class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        left=dummy
        right=dummy

        for _ in range(n+1):
            left=left.next
        
        while left:
            left=left.next
            right=right.next
        
        right.next=right.next.next

        return dummy.next

        
