class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        f = collections.Counter(s)
        
        last = None
        count = 0
        ans = []
        done = False
        h = []
        
        for k in f.keys():
            heapq.heappush(h, (-(ord(k) - ord('a')), k))
        
        while not done:
            done = True
            
            if len(h) > 0:
                k, c = heapq.heappop(h)
                
                if last != c or (count + 1 <= repeatLimit):
                    ans.append(c)
                    if last == c:
                        count += 1
                    else:
                        count = 1
                    last = c
                    f[c] -= 1
                    done = False
                    if f[c] > 0:
                        heapq.heappush(h, (k, c))
                else:
                    if len(h) == 0:
                        break
                    k2, c2 = heapq.heappop(h)

                    ans.append(c2)
                    if last == c2:
                        count += 1
                    else:
                        count = 1
                    last = c2
                    f[c2] -= 1
                    done = False
                    heapq.heappush(h, (k, c))
                    if f[c2] > 0:
                        heapq.heappush(h, (k2, c2))

        return "".join(ans)    