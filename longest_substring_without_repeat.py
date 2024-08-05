
# 3, longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if  s=="" :
            return 0
        l=r=0
        m=1
        for x in range(1,len(s)):
            if s[x] not in s[l:r+1]:
                r+=1
                m=max(m,r-l+1)
                continue
            else:
                print("inside else",s[l:r+1],"current x",s[x])
                r+=1
                while s[l]!=s[x]:
                    l+=1
                l+=1
        return m

s=Solution()
print(s.lengthOfLongestSubstring("pwawkew"))