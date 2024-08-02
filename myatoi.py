def myAtoi(s: str) -> int:
        newint='0'
        flag=0
        for i in s:
            if i in['-','+'] and len(newint)==1:
                if i=='-':
                    flag=1
                newint+='0'
                continue
            elif i==' ' and len(newint)==1:
                continue
            if not i.isdigit():
                break
            elif i.isdigit():
                newint+=i
        if int(newint)>2**31:
            newint=2**31 
            if not flag:
                return newint-1
            return -newint
        if flag==1:
            return -int(newint)
        return int(newint)
    
print(myAtoi("    +110aa11a"))
        