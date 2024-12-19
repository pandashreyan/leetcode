class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        INF = 10 ** 20
        
        def chunk_good(index, mn, mx, count):
            return mn == index - count and mx == index - 1
        
        def go(index, mn, mx, count):
            if index == N:
                if chunk_good(index, mn, mx, count):
                    return 1
                return -INF
            
            best = -20
            
            # take - end this chunk
            if chunk_good(index, mn, mx, count):
                best = max(best, go(index + 1, arr[index], arr[index], 1) + 1)
            
            # no take - continue this chunk
            best = max(best, go(index + 1, min(mn, arr[index]), max(mx, arr[index]), count + 1))
            return best
            
        return go(1, arr[0], arr[0], 1)