a,b=map(int,input().split())
s1alco=0
s2alco=0

for i in range(a):
    v,c=map(int,input().split())
    s1alco+=v*c
for i in range(b):
    v,c=map(int,input().split())
    s2alco+=v*c    

if s1alco==s2alco:
    print("same")
else:
    print("different")
             