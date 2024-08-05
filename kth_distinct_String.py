class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        x=0
        el={}
        
        for element in arr:
            if element not in el:
                el[element] =1
                x+=1
                if x == k:
                    return element
            else:
                
                
        return ""
       
s=Solution()
print(s.kthDistinct(["d","b","c","b","c","a","e","f","g"],2))