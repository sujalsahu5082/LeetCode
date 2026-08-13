class SegmentTree:
    def __init__(self, s):
        self.n = len(s)

        # left_char, right_char,
        # left_len, right_len, max_len, segment_length
        self.tree = [None] * (4 * self.n)

        self.s = s
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            c = self.s[l]
            self.tree[node] = (c, c, 1, 1, 1, 1)
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def merge(self, a, b):
        lc1, rc1, ll1, rl1, mx1, len1 = a
        lc2, rc2, ll2, rl2, mx2, len2 = b

        left_char = lc1
        right_char = rc2

        left_len = ll1
        right_len = rl2

        max_len = max(mx1, mx2)

        # The suffix of left and prefix of right can join
        if rc1 == lc2:

            max_len = max(max_len, rl1 + ll2)

            # Entire left segment has one character
            if ll1 == len1:
                left_len = len1 + ll2

            # Entire right segment has one character
            if rl2 == len2:
                right_len = rl1 + len2

        return (
            left_char,
            right_char,
            left_len,
            right_len,
            max_len,
            len1 + len2
        )

    def update(self, node, l, r, idx, char):
        if l == r:
            self.tree[node] = (char, char, 1, 1, 1, 1)
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, char)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, char)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query_max(self):
        return self.tree[1][4]


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        tree = SegmentTree(s)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(
                1,
                0,
                len(s) - 1,
                idx,
                char
            )

            ans.append(tree.query_max())

        return ans