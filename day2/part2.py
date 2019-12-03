#!/usr/local/bin/python3

input = "day2_input.txt"


def test_pair(noun, verb, list):
    list[1] = noun
    list[2] = verb

    opcode_pos = 0
    opcode = list[opcode_pos]
    while (opcode in [1, 2]):
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
        exit

    return list[0]

    


def main():
    with open(input, 'r') as fp:
        read  = fp.read()
        start = read[:-1].split(',')


    for noun in range(0, 100):
        for verb in range(0, 100):
            ints  = [int(i) for i in start]

            output = test_pair(noun, verb, ints)
            if (output == 19690720):
                print('Done! Noun: {}, Verb: {}.'.format(noun, verb))
                return

        
if __name__ == "__main__":
    main()
