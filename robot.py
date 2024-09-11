class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        inix=iniy=0
        d=0
        maxx=0
        maxy=0
        for x in commands:
            print(d,x,inix,iniy)
            if x ==-1:
                d+=1
                if d==4:
                    d=0
            elif x==-2:
                d-=1
                if d==-1:
                    d=3          
            else:
                if d ==0:
                    for _ in range(x):
                        iniy+=1
                        if [inix,iniy] in obstacles:
                                iniy-=1
                                maxx=max(maxx,abs(inix))
                                maxy=max(maxy,abs(iniy))
                                break
                   
                elif d==1:
                    for _ in range(x):
                        inix+=1
                        if [inix,iniy] in obstacles:
                                inix-=1
                                maxx=max(maxx,abs(inix))
                                maxy=max(maxy,abs(iniy))
                                break
                  
                elif d==2:
                    for _ in range(x):
                        iniy-=1
                        if [inix,iniy] in obstacles:
                                iniy+=1
                                maxx=max(maxx,abs(inix))
                                maxy=max(maxy,abs(iniy))
                                break
                   
                else:
                    print("inside else")
                    for _ in range(x):
                        inix-=1
                        print("1 subbed",inix)
                        if [inix,iniy] in obstacles:
                                inix+=1
                                maxx=max(maxx,abs(inix))
                                maxy=max(maxy,abs(iniy))
                                break
                maxx=max(maxx,abs(inix))
                maxy=max(maxy,abs(iniy))
        print(maxx,maxy)
        return maxy**2+maxx**2


S=Solution()    
print(S.robotSim([-2,8,3,7,-1],[]))