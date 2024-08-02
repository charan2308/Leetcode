import heapq,math
unsorted_list = [7, 3, 1,8,1,2,3]
# l=len(unsorted_list)
# print(math.log2(l))
# print(sorted(unsorted_list))
heapq.heapify(unsorted_list)
print(unsorted_list)
index=0
depth=int(math.log2(len(unsorted_list)))
for i in range(depth+1):
    print(" "*((2**(depth-i))-1),end="")
    for j in range(2**i):
        if index<len(unsorted_list):
            print(unsorted_list[index],end=" "*((2**(depth-i+1)-1)))
            index+=1
        else:
            break
        
    print("")


   1
 1   2
8 3 7 3