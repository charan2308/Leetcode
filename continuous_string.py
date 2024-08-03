class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        flag=0
        swapss=0
        first=nums[0]
        for x in range(len(nums)):
            if x==0:
                # print(x,"0 index")
                continue
            else:
                if nums[x]!=first and flag==0:
                    print(x,"first change")
                    if  
                    flag=1
                    continue
                if nums[x]==first and flag==1:
                    print(x,"first found")
                    
                    if int(not first) in nums[x+1:]:
                        print(x,"found to swap")
                        if nums[x]==first:
                            to_swap_index=-(nums[:x:-1].index(int(not(nums[x])))+1)
                            t=nums[x]
                            nums[x] = nums[to_swap_index]
                            nums[to_swap_index]=t
                            swapss+=1
                        elif nums[x]==nums[-1]:
                            t=nums[0]
                            nums[0]=nums[x]
                            first=nums[x]
                            nums[x]=t
                            
                    else:
                        print("broken")
                        break
                if nums[x]!=first and flag==1:
                    print(x,"same continue")
                    continue
        return swapss         

myclass=Solution()
input_val=[1,1,1,0,0,1,0,1,1,0]
input_val=[0,0,0,1,1,0,1,0,0,1]
input_val=[0,1,0,0,1,0,0,0,1]

print(myclass.minSwaps(input_val))

