class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(-(-pile // k) for pile in piles)

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if hours_needed(mid) <= h:   # mid works — try slower (smaller k)
                high = mid
            else:                        # mid too slow — must go faster
                low = mid + 1
        return low