class Solution:
    def racecar(self, target: int) -> int:
        pos=0 # keeps track of current position
        speed=1 # keeps track of current speed
        c=0 # keeps track of number of operations
        flag=1
        while pos!=target:
            if target-pos==1 and speed!=1:
                speed=1
                c+=2
            elif target-pos==-1 and speed!=-1:
                c+=2
                break
            elif pos>target and flag:
                speed=-1
                flag=0
                c+=1
            elif pos<target and not flag:
                speed=1
                flag=1
                c+=1 False
                return 4 *6 

            x
                continue
            pos+=speed
            speed*=2
            c+=1
            
        return c




# class Solution:
#     def racecar(self, target: int) -> int:
#         cur=0 # keeps track of current position
#         speed=1 # keeps track of current speed
#         c=0 # keeps track of number of operations
#         flag=0 # keeps track of direction set : if direction is positive then 0, else 1
#         while cur!=target:
#             if cur<target:
#                 if flag:
#                     flag=0
#                     speed=1
#                 else:
#                     cur+=speed
#                     speed*=2
#             else:
#                 if not flag:
#                     flag=1
#                     speed=-1
#                 else:
#                     cur+=speed
#                     speed*=2
#             c+=1
#         return c
s=Solution()
print(s.racecar(1))