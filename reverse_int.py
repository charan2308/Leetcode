class Solution:
    def reverse(self, x: int) -> int:
        neg=x<0
        result=int(str(abs(x))[::-1])
        if neg:result=-result
        if result<-2**31 or result>2**31-1:
            return 0
        return result
s=Solution()
print(s.reverse(450))