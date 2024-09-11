class Solution:
    def strangePrinter(self, s: str) -> int:
        prev=s[0]
        c=1
        for x in s: 
            if x!=prev :
                if x!=s[0]:
                    c+=1
                prev=x
        return c
s=Solution()
print(s.strangePrinter("tgbtgbt"))