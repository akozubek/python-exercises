
def get_value(reg, registers):
    if reg.isalpha():
        try:
            return registers[reg]
        except:
            return 0
    else:
        return int(reg)

def count_mul(instructions):
    registers = dict()
    for r in 'abcdefgh':
        registers[r] = 0

    mults = 0
    i = 0
    while i < len(instructions):
        instr = instructions[i]
        elems = instr.split(' ')
        reg = elems[1]
        if instr.startswith('set'):
           value = get_value(elems[2], registers)
           registers[reg] = value
        elif instr.startswith('sub'):
           value = get_value(elems[2], registers)
           registers[reg] = get_value(reg, registers) - value
        elif instr.startswith('mul'):
           value = get_value(elems[2], registers)
           registers[reg] = get_value(reg, registers) * value
           mults += 1
        elif instr.startswith('jnz'):
           x = get_value(reg, registers)
           y = get_value(elems[2], registers)
           if x != 0:
               # perform jump, subtract -1 so that you can safely add 1 later
               i = i + y - 1
        i += 1

    return mults


with open("day23.txt") as file:
    print("Result:", count_mul([line[:-1] for line in file.readlines()]))

# Part 2
h = 0
for x in range(109300,126300 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
print("Result 2:", h)
