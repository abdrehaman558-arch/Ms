n=int(input())

totalknot=list(map(int,input().split()))

total_learnedknot=list(map(int,input().split()))

missing_knot=sum(totalknot)-sum(total_learnedknot)
print(missing_knot)