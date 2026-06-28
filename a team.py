n=int(input())
solved_problem=0
for i in range(n):
    patya,vasya,tony=map(int,input().split())
    total_sure=patya+vasya+tony
    if total_sure>=2:
        solved_problem=solved_problem+1
print(solved_problem)      

   