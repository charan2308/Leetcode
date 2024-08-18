class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        final=[]
        visited=[]
        candidates.sort()
        def recursive(candidates,target,partial=[],s=0):
            print(partial,s)
            visited.append(partial)

            if s==target:
                if partial not in final:
                    final.append(partial)
                return 
            
            if s>target:
                return 
            
            for i in range(len(candidates)):
                
                n=candidates[i]
                if s+n>target:
                    break
                remaining=candidates[i+1:]
                if partial+[n] not in visited:
                    recursive(remaining,target,partial+[n],s+n)
        recursive(candidates,target)        
        return final



candidates=[10,1,2,7,6,1,5]
target=8
s=Solution()

print(s.combinationSum2(candidates, target))
