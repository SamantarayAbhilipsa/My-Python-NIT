p=float(input("enter the principal amount:"))
n=float(input("enter the number years:"))
r=float(input("enter the rate of interest:"))
CI=p*(pow((1+r/100),n))
print(f"compound interest:{CI}")

