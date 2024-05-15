def main():
    outfile = open("write_number.txt","w")
    num1 = int(input("Enter a number here"))
    num2 = int(input("Enter a number here"))
    num3 = int(input("Enter a number here"))
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    outfile.close()
    print("Writing process is completed")

main()