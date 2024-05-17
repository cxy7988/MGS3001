def main():
    infile = open("sales.txt","r")
    msum = 0
    time = 0
    for line in infile:
        line = infile.readline()
        msum += float(line)
        time = time + 1
    infile.close()
    print(f"The sum of sales is {msum}")
    print(f"The average of sale is {msum/time:.2f}")
    print("Process ends")

main()