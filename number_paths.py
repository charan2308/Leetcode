class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        from heapq import heappop,heappush
        neighbors={}
        for x in range(n):
           neighbors[x]=[]
        for s,d,t in roads:
            neighbors[s].append((d,t))
            neighbors[d].append((s,t))        
        MOD=10**9+7
        # queue=[(0,0,[0])]
        # count=0
        # mini=float('inf')
        # visited=set()
        # while queue:
        #     curtime,curnode,curpath=heapq.heappop(queue)
        #     visited.add(curnode)
        #     if curnode==n-1 and curtime<=mini:
        #         mini=curtime
        #         count+=1
        #     for neighbor,cost in neighbors[curnode]:
        #         if cost+curtime<=mini and neighbor not in visited:
        #             heapq.heappush(queue,(cost+curtime,neighbor,curpath+[neighbor]))
        
        # if count:
        #     return count
        # return -1
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]  # (time, node)
        
        while pq:
            cur_time, u = heappop(pq)
            
            if cur_time > dist[u]:
                continue
            
            for v, time in neighbors[u]:
                new_time = cur_time + time
                
                if new_time < dist[v]:
                    dist[v] = new_time
                    ways[v] = ways[u]
                    heappush(pq, (new_time, v))
                elif new_time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1] % MOD

s=Solution()
print(s.countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
