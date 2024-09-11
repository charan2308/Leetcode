class Solution:
    def findComplement(self, num: int) -> int:
        bina=""
        while num>0:
            r=num%2
            bina=str(int(not r))+bina
            num=num//2
        result=0
        print(int(bina,2))
        for i in range(len(bina)-1,-1,-1):
            if bina[-(i+1)]=='1':
                result+=2**i

        return result
s=Solution()
print(s.findComplement(100))