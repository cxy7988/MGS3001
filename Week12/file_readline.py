def main():
    friendlist = open("friendlist.txt", "r")
    for i in range(3):
        friends_name = friendlist.readline()
        print(friends_name)
    friendlist.close()


main()