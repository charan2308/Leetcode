class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        l=[]
        l.append([rStart,cStart])
        currow=rStart 
        curcol=cStart
        tot=rows*cols
        direction=1     #keeps track of the direction (1:right, 2:down,3:left,4:up)
        spiral=1
        while(len(l)<tot):
                if direction==1:
                    if spiral!=1:
                        spiral+=1
                    for i in range(spiral):
                        curcol+=1
                        if (-1<curcol<cols) and (-1<currow<rows):
                            l.append([currow,curcol])
                    direction+=1

                elif direction==2:
                    for i in range(spiral):
                        currow+=1
                        if (-1<curcol<cols) and (-1<currow<rows):
                            l.append([currow,curcol])
                    direction+=1
                elif direction==3:
                    spiral+=1
                    for i in range(spiral):
                        curcol-=1
                        if (-1<curcol<cols) and (-1<currow<rows):
                            l.append([currow,curcol])
                    direction+=1

                else:
                    for i in range(spiral):
                        currow-=1
                        if (-1<curcol<cols) and (-1<currow<rows):
                            l.append([currow,curcol])
                    direction=1
        return l


s=Solution()
print(s.spiralMatrixIII(5,6,1,4))