def red(x):
    fin=0
    a=0
    b=0
    count=0
    while(x>0):
        fin=0
        print(x)
        for i in range(2,x):
           
            if x%i==0:
                a=i
                b=x//i
                fin=max(a,b)
            
                
        if fin!=0:
            x=fin
            count+=1
        else:
            x-=1
            count+=1
    return count

val=int(input("Enter the number:"))
print(red(val))

 