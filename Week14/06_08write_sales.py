def main():
    num_tran = int(input("For how many times do you want for sales"))
    outfile = open('sales.txt',"w")
    for i in range(num_tran):
        sales = float(input(f"Enter the sales for transaction{i}"))
        outfile.write(str(sales)+"\n")
    outfile.close()


if __name__ == '__main__':
    main()