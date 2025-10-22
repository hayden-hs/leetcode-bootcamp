# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        sec = slow.next
        prev = slow.next = None
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp
        

        #idea:
        l, r = head, prev
        while r:
            l_temp = l.next
            r_temp = r.next

            l.next = r
            r.next = l_temp

            l = l_temp
            r = r_temp

            