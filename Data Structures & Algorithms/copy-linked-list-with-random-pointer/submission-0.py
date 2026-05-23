class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        old_to_new = {}

        curr = head

        # First pass:
        # create all copied nodes
        while curr:

            copy = Node(curr.val)

            old_to_new[curr] = copy

            curr = curr.next

        curr = head

        # Second pass:
        # connect next and random
        while curr:

            copy = old_to_new[curr]

            copy.next = old_to_new.get(curr.next)

            copy.random = old_to_new.get(curr.random)

            curr = curr.next

        return old_to_new[head]