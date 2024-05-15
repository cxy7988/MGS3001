def main():
    infile = open("write_number.txt","r")
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    sum = num1 + num2 + num3
    print(f"The sum is {sum}")
    infile.close()


main()
