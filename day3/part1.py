#!/usr/local/bin/python3

import sys

def split_paths(path):
    split_path = path.split(',')
    split_path = [(step[0], int(step[1:])) for step in split_path]

    return split_path


def calc_positions(steps):
    # start at (0,0)
    # d - direction, l - length
    ps = []
    x = 0
    y = 0
    for (d, l) in steps:
        if (d == 'R'):
            for i in range(1,l+1):
                x += 1
                ps.append([x,y])
        elif (d == 'U'):
            for i in range(1,l+1):
                y += 1
                ps.append([x,y])
        elif (d == 'L'):
            for i in range(1,l+1):
                x -= 1
                ps.append([x,y])
        elif (d == 'D'):
            for i in range(1,l+1):
                y -= 1
                ps.append([x,y])
        else:
            print("Error: Direction = {}.".format(d))
            exit(1)

    return(ps)


def main():
    with open(sys.argv[1], 'r') as fp:
        total = 0
        wire1 = fp.readline()
        wire2 = fp.readline()

    w1_steps = split_paths(wire1)
    w2_steps = split_paths(wire2)

    w1_ps = calc_positions(w1_steps)
    w2_ps = calc_positions(w2_steps)

    # closest collision
    cc = -1
    for p in w1_ps:
        if (p in w2_ps):
            dist = abs(p[0]) + abs(p[1])
            if (cc == -1):
                cc = dist
            elif (dist < cc):
                cc = dist

    print(cc)


if __name__ == "__main__":
    main()
