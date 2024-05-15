def main():
    infile = open("sales.txt","r")
    line = infile.readline()
    sum = 0
    time = 0
    while line != "":
        sum = sum + float(line)
        line = infile.readline()
        time = time + 1

    infile.close()
    print(f"The sum of sales is {sum}")
    print(f"The average of sale is {sum/time:.2f}")
    print("Process ends")

main()