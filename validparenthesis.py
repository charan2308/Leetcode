class Solution:
    def isValid(self, s: str) -> bool:
        mylist=[]
        for a in s:

            if a in ["(","[","{"]:
                mylist.append(a)
            elif not mylist:
                return False
            elif a ==")" and mylist[-1]=="(":
                    mylist.pop()
            elif a=="}" and mylist[-1]=="{":
                mylist.pop()
            elif a=="]" and mylist[-1]=="[":
                mylist.pop()
            
            else:
                return False
        if not mylist:
                return True
x=Solution()
print(x.isValid("()"))
                                