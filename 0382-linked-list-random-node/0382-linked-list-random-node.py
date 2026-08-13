import random

class Solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        curr = self.head
        ans = curr.val
        i = 1

        while curr:
            if random.randint(1, i) == 1:
                ans = curr.val

            curr = curr.next
            i += 1

        return ans