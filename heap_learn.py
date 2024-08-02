#Program to practice heap
## Example questions : 
# Find the Kth smallest element in the list of unsorted elements
# Find the Kth largest element in the list of unsorted elements




import math
import heapq,math
import time
unsorted_list = [
    37, 23, 14, 90, 81, 45, 78, 26, 55, 16,
    67, 83, 11, 99, 74, 58, 49, 22, 71, 34,
    3, 88, 65, 53, 47, 97, 20, 59, 92, 76,
    43, 39, 50, 84, 32, 8, 19, 61, 95, 86,
    18, 29, 72, 41, 13, 7, 35, 57, 68, 24,
    85, 52, 1, 66, 93, 79, 31, 46, 9, 5,
    44, 21, 82, 15, 4, 62, 40, 56, 25, 91,
    73, 33, 30, 48, 69, 12, 75, 28, 54, 6,
    87, 60, 38, 27, 42, 10, 98, 64, 89, 77,
    2, 63, 17, 51, 70, 94, 80, 36, 100, 96
]
k=2
unsorted_list = [
     37, 23, 14, 90, 81, 45]
# l=len(unsorted_list)
# print(math.log2(l))
# print(sorted(unsorted_list))
heapq.heapify(unsorted_list)
print(unsorted_list)
for i in range(math.log(len(unsorted_list))):
    print("newline")

# print(unsorted_list)
# for x in range(int(math.log2(l))+1):
#     for y in range (x,(2*x)+1):
#         if y<l:
#             print(unsorted_list[y],end=" ")
#     print()

# start_time = time.time()
# unsorted_list = [
#     37, 23, 14, 90, 81, 45]
# myheap=[]
# heap_length=0
# for x in range(len(unsorted_list)) :
#     heapq.heappush(myheap,-unsorted_list[x])
#     heap_length+=1
#     print("current heap before pop",myheap)

#     if heap_length>k:
#         heapq.heappop(myheap)
#         print("current heap after pop",myheap)
# print(-myheap[0])
# heapq.heapify(unsorted_list)
# fifth_smallest = heapq.nsmallest(5, unsorted_list)[-1]
# print(fifth_smallest)
# print(time.time()-start_time)

# unsorted_list = [
#     37, 23, 14, 90, 81, 45, 78, 26, 55, 16,
#     67, 83, 11, 99, 74, 58, 49, 22, 71, 34,
#     3, 88, 65, 53, 47, 97, 20, 59, 92, 76,
#     43, 39, 50, 84, 32, 8, 19, 61, 95, 86,
#     18, 29, 72, 41, 13, 7, 35, 57, 68, 28,
#     85, 52, 1, 66, 93, 79, 31, 46, 9, 5,
#     44, 21, 82, 15, 4, 62, 40, 56, 25, 91,
#     73, 33, 30, 48, 69, 12, 75, 28, 54, 6,
#     87, 60, 38, 27, 42, 10, 98, 64, 89, 77,
#     2, 63, 17, 51, 70, 94, 80, 36, 100, 96
# ]
# start_time=time.time()
# da=sorted(unsorted_list)
# print(da[k-1])
# print(time.time()-start_time)    