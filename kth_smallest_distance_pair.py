import heapq
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        l=[]
        heapq.heapify(l)
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)) :
                diff=abs(nums[i]-nums[j])
                if k==0 and diff<-l[0]:
                    print("hi",l[0])
                    heapq.heappop(l)
                    heapq.heappush(l,-diff)
                    
                    
                    continue
                
                heapq.heappush(l,-diff)
                k-=1
                pow(    )

                
            
            
        print(l)

        return -l[0]





s=Solution()
s.smallestDistancePair([3,5,2,6,7,8,1],2)