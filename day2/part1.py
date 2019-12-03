#!/usr/local/bin/python3

input = "day2_input.txt"



def main():
    with open(input, 'r') as fp:
        list = fp.read()
        list = list[:-1].split(',')
        list = [int(i) for i in list]

        list[1] = 12
        list[2] = 2

    opcode_pos = 0
    opcode = list[opcode_pos]
    while (opcode in [1, 2]):
        #list[opcode_pos+1] = 12
        #list[opcode_pos+2] = 2

        in1 = list[opcode_pos+1]
        in2 = list[opcode_pos+2]
        out = list[opcode_pos+3]

        if (opcode == 1):
            list[out] = list[in1] + list[in2]
            
        if (opcode == 2):
            list[out] = list[in1] * list[in2]

        opcode_pos += 4
        opcode = list[opcode_pos]


    if (opcode != 99):
        print("Failed!")
        return

    print('Done! Position 0 is: {}.'.format(list[0]))

        
if __name__ == "__main__":
    main()
