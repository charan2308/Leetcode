class Solution:
    def firstUniqChar(self, s: str) -> int:
        empty={}
        for letter in s:
            if letter in empty:
                empty[letter] +=1
            else:
                empty[letter] =1
        for i in empty:
            if empty[i] ==1:
                return s.index(i)
        return -1

mysol=Solution()
print(mysol.firstUniqChar("aaab"))