total = 0
starting = int(input("Enter starting number: "))
ending = int(input("Enter ending number: "))
for num in range(starting,ending+1):
    total = total + num
    print(total)