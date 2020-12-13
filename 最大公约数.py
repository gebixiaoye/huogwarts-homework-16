def gcd(x,y):
    min1=min(x,y)
    while min1>1:
        if (x%min1!=0) or (y%min1!=0):
            min1-=1
        else :
            print( min1)
            break
            
