def main():
    num_emp = int(input("How many employees are in the company?"))
    outfile = open("write_emp_record.txt","w")
    for i in range(num_emp):
        emp_name = input(f"Employee #{i+1} name: ")
        emp_id = input(f"Employee #{i+1} ID: ")
        emp_dept = input(f"Employee #{i+1} department: ")
        outfile.write(emp_name+"\n")
        outfile.write(emp_id+"\n")
        outfile.write(emp_dept+"\n")
        print("")

    outfile.close()
    print("The employee records have been saved")


main()