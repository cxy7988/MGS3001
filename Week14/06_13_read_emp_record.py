def main():
    infile = open("write_emp_record.txt","r")
    name = infile.readline()
    while name != "":
        id = infile.readline()
        dept = infile.readline()
        name = name.rstrip("\n")
        id = id.rstrip("\n")
        dept = dept.rstrip("\n")
        print(f"Name: {name}\nID: {id}\nDepartment: {dept}")
        print("")
        name = infile.readline()


main()