x=input("Enter a list of numbers:")
y=x.split(",")
z=int(input("Enter the index to retrieve:"))
if z<len(y):
    val=y[z]
    print("The value at index is:",val)
else:
    print("Index is out of range")