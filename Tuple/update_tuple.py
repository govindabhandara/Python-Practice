x=("apple","banana","kiwi")
y=list(x)
y[1]="cherry"
x=tuple(y)
print(x)