# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # slow pointer start from head
        fast = head # start with head fast pointer 

        while fast and fast.next: # while fast is true and has .next we can run the loop
            slow = slow.next # moving slow +1 step
            fast = fast.next.next # moving fast +2 step 

            if slow == fast: # if the be at the same spot with steps 
                return True # we have  a loop if the have got to the same spot

        return False 