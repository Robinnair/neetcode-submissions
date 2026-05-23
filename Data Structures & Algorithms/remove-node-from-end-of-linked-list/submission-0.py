# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp!=None):
            temp=temp.next
            count+=1
        target=count-(n-1)
        index=1
        temp=head
        prev=None
        while(temp!=None):
            if(index==target):
                if prev is None:
                    head=head.next
                    break
                else:
                    prev.next=temp.next
                    break
            prev=temp
            temp=temp.next
            index+=1
        return head
