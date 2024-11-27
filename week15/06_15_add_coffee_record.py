def main():
    proceed = "y"
    outfile = open("coffee.txt","a")
    while proceed == "y":
        description = input("Enter the description of coffee bean here")
        quantity = input("Enter the quantity of coffee here")
        outfile.write(f"description: {description}")
        outfile.write("\n")
        outfile.write(f"quantity: {quantity}")
        outfile.write("\n")
        proceed = input("Do you want to continue(y/n)")
    outfile.close()
    print("Data appended to coffee.txt")

main()