# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        temp=head
        while temp!=None:
            temp=temp.next
            l+=1

        slow=head
        if slow is None:
            return slow
        fast=slow.next
        while fast!=None:
            if slow.val==fast.val:
                slow.next=slow.next.next
                fast=slow.next
            else:
                slow=slow.next
                fast=fast.next
        return head
            

        