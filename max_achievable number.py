class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for _ in range(t):
            num=num+2
        return num
s=Solution()
print(s.theMaximumAchievableX(3,2))        