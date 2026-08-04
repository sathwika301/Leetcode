# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head==None or head.next==None:
            return head
        while temp.next!=None:
            if temp.next.val==temp.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
            

        