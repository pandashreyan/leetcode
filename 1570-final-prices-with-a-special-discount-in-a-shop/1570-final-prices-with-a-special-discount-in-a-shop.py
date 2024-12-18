class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        INF = 10 ** 20
        
        stack = [-INF]
        ans = []
        for i in range(N - 1, -1, -1):
            x = prices[i]
            
            while stack[-1] > x:
                stack.pop()
                
            ans.append(x - max(stack[-1], 0))
            stack.append(x)
        ans.reverse()
        return ans