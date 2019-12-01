#!/usr/local/bin/python3

input = "day1_input.txt"

def calc_fuel(mass):
    if mass <= 0:
        return 0

    fuel = (mass // 3) - 2
    if (fuel < 0):
        fuel = 0
    return (fuel + calc_fuel(fuel))

def main():
    with open(input, 'r') as fp:
        total = 0
        mass = fp.readline()
        while (mass):
            total += calc_fuel(int(mass))
            mass = fp.readline()

    print(total)


if __name__ == "__main__":
    main()
