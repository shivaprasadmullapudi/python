from pickletools import float8


x=int(input("Enter the number of days: "))
n=int(input("Enter the Captial: "))
#percentage should be mentioned in decimals like 10% will 0.1
per=float(input("Enter the percentage:"))
for i in range(x) :
    p=n*per
    n=n+p
    print(f"Day {i} and profit {n}")
    
