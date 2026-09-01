from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter
        sr = sc = 0
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)

        # All litter collected
        full_mask = (1 << total) - 1

        # BFS:
        # (row, col, mask, remaining_energy)
        q = deque()
        q.append((sr, sc, 0, energy))

        # For each (row, col, mask),
        # store the maximum energy we have had there.
        best = {}
        best[(sr, sc, 0)] = energy

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            # Process one BFS level
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                # All litter collected
                if mask == full_mask:
                    return moves

                # No energy means we cannot make another move
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Spend 1 energy for the move
                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # If we have already reached this state
                    # with more/equal energy, skip it.
                    if key in best and best[key] >= ne:
                        continue

                    # We reached it with better energy
                    best[key] = ne
                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1