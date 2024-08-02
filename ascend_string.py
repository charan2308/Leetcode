def areNumbersAscending( s: str) -> bool:
    prev=-1
    for i in s.split():
        if i.isnumeric():
            if prev==-1 :
                prev = i
                continue
            if int(i)<=int(prev) :
                return False
            prev = i

    return True
        
print(areNumbersAscending("11 box has 33 blue 44 red 66 green and 120 yellow marbles"))