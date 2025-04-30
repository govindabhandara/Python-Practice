# Check if a number is a power of 2 using (n & (n - 1)) == 0.
n=int(input("enter"))
is_power_of_two=n>0 and (n&(n-1))==0
print(is_power_of_two)
