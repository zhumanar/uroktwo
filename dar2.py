s="intoomr"
n=len(s)
print(n)
s1=""
s2=""
for i in range(n-2,-1,-2):
    s1=s1+s[i]
if n%2==1:
    l=0
else:
    l=1
for i in range(l,n,2):
    s2=s2+s[i]

s3=s1+s2
print(s3)
