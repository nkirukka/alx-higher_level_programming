#!/usr/bin/python3


if __name__ == "__main__":
    import hidden_4

    sortedList = dir(hidden)
    for name in sortedList:
        if not name.startswith("__"):
            print("{:s}".format(name))
