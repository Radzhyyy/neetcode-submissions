# Definition for singly-linked list.
# class Listail:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[Listail]) -> Optional[Listail]:
        dummy = ListNode() # create start node

        tail = dummy # pointer start at dymmy

        while list1 and list2: # loop as long as list1 and list two have nodes togather
            if list1.val < list2.val: # checking value of the nodes to start with lowest
                tail.next = list1 # moving tail next to curr list 1
                list1 = list1.next # moving list1 head to next node
            
            else:
                tail.next = list2 # moving tail to list2 if val is smaller then list1
                list2 = list2.next # moving list2 headto next node 

            tail = tail.next # moving tail to the last conncted node 

        tail.next = list1 or list2 # moving tail pointer to rest of the nodes 

        return dummy.next # retirn to start output 

