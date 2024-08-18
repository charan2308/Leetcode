def printing(nums,partial=[]):
    print(partial)
    for i in range(len(nums)):
        n=nums[i]
        remaining=nums[i+1:]
        printing(remaining,partial+[n])

printing([1,2,3,4])