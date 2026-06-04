d=float(input())
w=float(input())
n=int(input())
pi=3.14159

total_space_needed=n*w
circumfranceof_table=pi*d
if circumfranceof_table>=total_space_needed:
    print("yes")
else:
    print("no")    