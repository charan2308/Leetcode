class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from heapq import heappop,heappush
        neighbors={}
        for x in range(n):
            neighbors[x]=[]
        for s,d,c in flights:
            neighbors[s].append((d,c))
        # print(neighbors)
        
        queue=[(0,0,src,[src])]
        newpath=[float("inf")]*n
        newpath[src]=0
        while queue:
            
            curstops,curcost,curnode,curpath=heappop(queue)

            if curstops>k:
                continue
            
            for neighbor,cost in neighbors[curnode]:
                if curcost+cost<newpath[neighbor] and curstops<=k:
                    newpath[neighbor]=curcost+cost
                    heappush(queue,(curstops+1,curcost+cost,neighbor,curpath+[neighbor]))
        print(newpath)  
        print(curpath)
        if  newpath[dst]==float('inf'):
            return -1     
        return newpath[dst]

    
            
                
            
        

s=Solution()
cost=s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1)
# # cost,path=s.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]]
# # ,0,2,1)
# cost=s.findCheapestPrice(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,3,1)

print(cost)