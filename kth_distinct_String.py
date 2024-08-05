class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        em=[]
        for element in arr:
            if arr.count(element) == 1:
                em.append(element)
        return em[k-1]
s=Solution()
print(s.kthDistinct(["d","b","c","b","c","a"],2))