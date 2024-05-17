def main():
    outfile = open("write_video_time.txt","w")
    time = int(input("How many videos are in the project?"))
    print("Enter Enter the running times for each video.")
    for i in range(time):
        video_time = float(input(f"video #{i+1}: "))
        outfile.write(str(video_time) + '\n')

    outfile.close()
    print("The times have been saved to video_times.txt.")


main()