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
        queue=[(0,0)]
        dist=[float('inf')]*n
        dist[0]=0
        ways=[0]*n
        ways[0]=1        
        while queue:
            curtime,curnode=heappop(queue)
            if curtime>dist[curnode]:
                continue
            for node,time in neighbors[curnode]:
                newtime=curtime+time
                if newtime<dist[node]:
                    dist[node]=newtime
                    ways[node]=ways[curnode]
                    heappush(queue,(newtime,node))
                elif newtime==dist[node]:
                    ways[node]=(ways[node]+ways[curnode])%MOD
                    
        return ways[n-1] %MOD

s=Solution()
print(s.countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
