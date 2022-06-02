#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4.pyc import hidden
    sortedList = sorted(hidden)
    for name in sortedList:
        if name[0] != "_" and name[1] != "_":
            print(name)
