class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        # objective : find  the min and max elements in diff arrays and get their difference whose difference is max 
        # mini=arrays[0][0]
        
        # maxi=0
        # d={}
        # d[mini]=[[0,mini]]
        # d[maxi]=[]
        # sec_max=0
        # sec_min=0
        # for x in range(len(arrays)): 
        #     if arrays[x][0]<mini:
        #         mini=arrays[x][0]
        #         d[mini].append([])
        #         # /how about we keep track of the max element and the array which it belongs to , and min element and the array which it belongs to .huu. and, if both are same array , we need the 2nd largest or smallest element alva it will be max of another ele ashte alva
        #         # ?? can try
        #     if arrays[x][-1]>maxi and d[mini]!=x:
        #         maxi=arrays[x][-1]
        # return abs(mini-maxi)
        #     # shouldnt i find the max and min amongst huu all arrays ?  how do we do that?dict? can we see if max is also from the same x?okayyy . what do we add in dict ? x[0]:x if x is int from 0 to len .huuu 
        global_max=0
        mini=arrays[0][0]
        maxi=arrays[0][-1]
        for i in range(1,len(arrays)):
            x=arrays[i]
            global_max=max(global_max,x[-1]-mini,maxi-x[0])
            mini=min(mini,x[0])
            maxi=max(maxi,x[-1])
        return global_max   

    # understood pa?huu 
S=Solution() 
print(S.maxDistance([[1],[4]]))