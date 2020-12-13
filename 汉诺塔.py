def hnt(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hnt(n-1,x,z,y)
        print(x,'->',z)
        hnt(n-1,y,x,z)
        
teme=int(input('输入一个汉诺塔层数：'))
hnt(teme,'X','Y','Z')
