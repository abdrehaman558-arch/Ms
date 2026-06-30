x=input()
upper_count=0
lower_count=0
for char in x:
    if char.isupper():
        upper_count+=1
    else:
        lower_count+=1
if upper_count>lower_count:
    print(x.upper())
else:
    print(x.lower())
                    