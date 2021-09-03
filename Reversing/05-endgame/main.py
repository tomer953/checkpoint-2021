FLAG = """
1A 05 1B 03 AB AB EF 08 FF 80
1C B3 1D 91 BA CD EF 22 FF 80
1E 05 1F 05 CD EF EF 19 FF 80
1B 30 1D 08 DC BD EF 06 FF 80
1A 01 1B 02 CD AB 1B 05 CD AB
1C 1E CD AC 1E B2 1F 05 CD EF
CD AE 1B E7 1C C6 AB BC 1D C1
1E 62 AB DE 1F AD AB DF AB BD
AB AB 1B 04 CD AB 1B FA 1C FA
AB BC CD AB 1B F1 1C C8 AB BC
AB AB 1D 7D CD AD 1B FA 1C 04
CD BC 1F 68 BA BF CD AB 1C FD
AB AC 1C 64 CD AC 1B 0A 1C 40
CD BC CD AB 1B F3 1C 3A 1D DC
AB CD AB BC AB AB 1F 04 CD AF
1B 05 1C 64 CD BC CD AB 1B 03
1C 64 CD CB CD BC 1D 32 BA BD
CD AB 1F 03 CD CF 1B 44 AB CB
CD AC 1B 06 1C 0A CD BC CD BC
CD BC CD BC 1D 7B AB BD AB AB
1B C8 CD AB CD BC 1F 02 DC BF
1C 73 BA BC CD AB 1C 3E AB BC
AB AB CD FF CD AF 1C 35 AB BC
1D 02 DC BD CD AB 1B F9 AB AB
1C 0A CD AC DC CD AB AC CD AF
1B 01 AB AB 00 00
"""


def print_flag(a):
    hex_string = hex(int(a))[2:]
    ascii = bytes.fromhex(hex_string)
    ascii_string = ascii.decode("utf-8")
    print(ascii_string)
    pass

def apply_op(memory, op, x, y):
    if op == '+':
        memory[x] += int(memory[y])
    elif op == '-':
        memory[x] -= int(memory[y])
    elif op == '*':
        memory[x] *= int(memory[y])
    elif op == '/':
        memory[x] = int(memory[x]) / int(memory[y])

def main():
    code = FLAG.split()
    memory = {
        "1A": 0,
        "1B": 0,
        "1C": 0,
        "1D": 0,
        "1E": 0,
        "1F": 0,
    }
    operands = {
        "AB": "+",
        "BA": "-",
        "CD": "*",
        "DC": "/"
    }
    for i in range(0,len(code),2):
        cmd = code[i:i+2]
        # print(memory)

        # save to memory
        if cmd[0] in memory:
            memory[cmd[0]] = int(cmd[1],16)
            print(str(cmd) + '-> ' + cmd[0] + ' = ' + cmd[1])

        # apply operand
        elif cmd[0] in operands:
            op = operands[cmd[0]]
            x = "1" + cmd[1][0]
            y = "1" + cmd[1][1]
            print(str(cmd) + " : " + x + " = " + x + " " + op + " " + y)
            apply_op(memory, op, x, y)
            
        elif cmd[0] == '00':
            print('finish.. printing memory:')
            print(memory)
            print('flag:')
            print_flag(memory["1A"])
            
    pass


main()