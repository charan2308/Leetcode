class Solution:
    def minimumSum(self, num: int) -> int:
        # sort the num and combine the alt digits and then add sum
        s=list(str(num))
        s.sort()
        num1=s[0]+s[2]
        num2=s[1]+s[3]
        return int(num1)+int(num2)


s=Solution()
print(s.minimumSum(4009))