n=int(input())
hits=list(map(int,input().split()))
total=0
totalno_scores=0
for i in hits:
    if i!=-1:
        total+=i
        totalno_scores+=1
his_point=total/totalno_scores
print(his_point)        
        
        