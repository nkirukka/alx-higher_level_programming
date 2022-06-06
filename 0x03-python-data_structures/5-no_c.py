#!/usr/bin/python3


def no_c(my_string):
    new_list = list(my_string)
    new_str = ""

    for char in new_list:
        if char != "c" and char != "C":
            new_str += char
    return new_str


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
