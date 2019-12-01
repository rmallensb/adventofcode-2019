#!/usr/local/bin/python3

input = "day1_input.txt"

def main():
    with open(input, 'r') as fp:
        total = 0
        mass = fp.readline()
        while (mass):
            total += ((int(mass) // 3) - 2)
            mass = fp.readline()

    print(total)


if __name__ == "__main__":
    main()
