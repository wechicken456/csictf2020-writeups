from Crypto.Util.number import inverse

n1 = 86812553978993
n2 = 81744303091421 
n3 = 83695120256591
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409

t1 = c1*(n2*n3)*inverse(n2*n3,n1)
t2 = c2*(n1*n3)*inverse(n1*n3,n2)
t3 = c3*(n1*n2)*inverse(n1*n2,n3)
c = (t1+t2+t3)%(n1*n2*n3)
m = pow(c,1./3)
m = str(int(m))
print m
flag = "csictf{"
for i in range(0,len(m), 2):
    flag += chr(int(m[i:i+2],16))
flag += "}"
print flag

