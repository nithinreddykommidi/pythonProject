num=13
for i in range(2,num//2):
    if num%i == 0:
        print("non prime")
        break
else:
    print("prime")