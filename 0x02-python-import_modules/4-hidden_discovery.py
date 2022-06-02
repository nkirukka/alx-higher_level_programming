#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4
    sortedList = dir(hidden)
    for name in sortedList:
        if not name.startsWith("__"):
            print("{:s}".format(name))
