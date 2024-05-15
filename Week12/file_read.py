

def main():
    friendlist = open("friendlist.txt", "r")
    friends_name = friendlist.read()
    friendlist.close()
    print(friends_name)


if __name__ == '__main__':
    main()