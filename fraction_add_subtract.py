class Solution:
    def fractionAddition(self, expression: str) -> str:
        n=[]
        d=[]
        s=expression
        for i in range(len(s)):   # -5/2+10/3+7/9
            if s[i]=='1' and i!=len(s)-1 and s[i+1]=='0' :
                if i==0 or s[i-1]=='+':
                    n.append(10)
                elif s[i-1]=='-':
                    n.append(-10)
                elif s[i-1]=='/':
                    d.append(10)
                continue 
            if i==0 and s[0] not in ['-','+']:
                n.append(int(s[0]))
                continue
            elif s[i-1] in ['-','+']:
                if s[i-1]=='-':
                    n.append(-int(s[i]))
                else:
                    n.append(int(s[i]))
                continue
            elif s[i-1] =='/':
                d.append(int(s[i]))
        lcm=1
        for i in set(d):
            lcm=lcm*i 
        sum=0
        for i in range(len(n)):
            n[i]=n[i]*(lcm//d[i])
            sum+=n[i]
        def conv(a,b):
            minum= min(a,b)
            result=''
            if a%b==0 or b%a==0:
                if b>a:
                    result='1/'+str((b//a))
                    return result
                else:
                    result=str(a//b)+'/1'
                    return result
            flag=1
            while(flag):
                minum= min(a,b)
                flag=0
                for i in range(2,abs(minum//2+1)):
                    if a%i==0 and b%i==0:
                        a=a//i
                        b=b//i
                        flag=1
            result=str(a)+'/'+str(b)
            return result
        if sum==0:
            return '0/1'
        elif sum==-1 or sum==1:
            result= str(sum)+'/'+str(lcm)
            return result
        elif lcm==1:
            result=str(sum)+'/1'
            return result
        return(conv(sum,lcm))