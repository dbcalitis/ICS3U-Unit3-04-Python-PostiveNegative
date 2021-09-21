#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program checks if the number is a positive, negative or a zero


def main():
    # This function checks if the number is a positive, negative or a zero

    # input
    number = int(input("Enter an integer: "))

    # process and output
    if number < 0:
        print("{} is a negative number.".format(number))
    elif number > 0:
        print("{} is a positive number.".format(number))
    else:
        print("0 is just a zero.")

    print("\nDone.")


if __name__ == "__main__":
    main()
