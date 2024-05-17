def main():
    print("Here are the running times for each video:")
    infile = open("write_video_time.txt","r")
    i = 1
    total = 0
    for line in infile:
        total_second = float(line)
        hour = int(total_second//3600)
        minute = int((total_second-hour*3600)//60)
        second = float(line)-minute*60-hour*3600
        print(f"Video #{i}: {hour}h {minute}m {second:.1f}s")
        i += 1
        total = total+total_second
    infile.close()
    print(f"The total running time is {total} seconds")


main()