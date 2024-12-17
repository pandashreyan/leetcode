class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        events = collections.Counter()
        for x in nums:
            events[x - k] += 1
            events[x + k + 1] -= 1

        best = 0
        count = 0
        for key in sorted(events.keys()):
            count += events[key]
            best = max(best, count)
        return best