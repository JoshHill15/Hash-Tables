class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, head1, head2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current = ListNode()
        while not (head1 is None or head2 is None):

            # while not head1 is None or not head2 is None:

            if head1.val <= head2.val:
                temp = head1
                head1 = head1.next
            else:
                temp = head2
                head2 = head2.next

            current.next = temp
            current = current.next

        current.next = head1 or head2

        return dummy.next

    def merge_lists(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if (h1.val < h2.val):
            h1.next = self.merge_lists(h1.next, h2)
            return h1
        else:
            h2.next = self.merge_lists(h2.next, h1)
            return h2


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)

other = ListNode(1)
other.next = ListNode(3)
other.next.next = ListNode(4)
# ----------------------------
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(4)

other2 = ListNode(1)
other2.next = ListNode(3)
other2.next.next = ListNode(4)

a = ListNode()
b = ListNode()

sol = Solution()

ans = sol.mergeTwoLists(head, other)
recursive = sol.merge_lists(head2, other2)

m = []
r = []

while ans:
    m.append(ans.val)
    ans = ans.next

while recursive:
    r.append(recursive.val)
    recursive = recursive.next

print("iterative", m)
print("recursive", r)
