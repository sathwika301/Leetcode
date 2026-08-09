class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
       

        n = len(piles)

        # memo will store answers for states (index, M)
        memo = {}

        def solve(i, M):

            # If all piles are taken
            if i >= n:
                return 0

            # If we already solved this state
            if (i, M) in memo:
                return memo[(i, M)]

            # Total stones remaining from index i
            remaining = sum(piles[i:])

            # Best answer for the current player
            best = 0

            # Current player can take 1 to 2*M piles
            for X in range(1, 2 * M + 1):

                # Cannot take more piles than available
                if i + X > n:
                    break

                # After taking X piles,
                # it becomes the opponent's turn
                new_M = max(M, X)

                opponent = solve(i + X, new_M)

                # Whatever opponent finally gets,
                # the rest belongs to the current player
                current_player = remaining - opponent

                # Choose the move giving maximum stones
                best = max(best, current_player)

            # Save the answer for this state
            memo[(i, M)] = best

            return best

        # Alice starts from index 0 with M = 1
        return solve(0, 1)
        