print("number\tsquare")
print("---------------")

starting = int(input("Enter the starting number: "))
ending = int(input("Enter the ending number: "))

for a in range(starting, ending+1):
    print(a,"\t",a*a)