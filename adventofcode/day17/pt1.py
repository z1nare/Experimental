# Read the input file
with open("C:\\Users\\garba\\Downloads\\adventcode.csv", "r") as file:
    pages = [line.strip() for line in file]

# Extract the register values from the first lines
registers = {}
registers['A'] = int(pages[0].split(":")[1].strip())
registers['B'] = int(pages[1].split(":")[1].strip())
registers['C'] = int(pages[2].split(":")[1].strip())

# Extract the program from the last line
program = list(map(int, pages[4].split(":")[1].strip().split(",")))

# Function to decode combo operand values
def get_combo_value(operand, registers):
    if operand == 4:  # Register A
        return registers['A']
    elif operand == 5:  # Register B
        return registers['B']
    elif operand == 6:  # Register C
        return registers['C']
    elif operand in [0, 1, 2, 3]:  # Literal values 0-3
        return operand
    else:
        raise ValueError("Invalid combo operand: " + str(operand))

# Execute the program
def run_program(registers, program):
    output = []  # To store outputs from "out" instructions
    instruction_pointer = 0  # Start at the first opcode

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]  # Fetch opcode
        operand = program[instruction_pointer + 1]  # Fetch operand

        if opcode == 0:  # adv - Divide A by 2^operand
            power = get_combo_value(operand, registers)
            registers['A'] //= (2 ** power)

        elif opcode == 1:  # bxl - B XOR operand
            registers['B'] ^= operand

        elif opcode == 2:  # bst - B = operand % 8
            registers['B'] = get_combo_value(operand, registers) % 8

        elif opcode == 3:  # jnz - Jump to operand if A != 0
            if registers['A'] != 0:
                instruction_pointer = operand
                continue  # Do not increase pointer if jump occurs

        elif opcode == 4:  # bxc - B XOR C
            registers['B'] ^= registers['C']

        elif opcode == 5:  # out - Output operand % 8
            value = get_combo_value(operand, registers) % 8
            output.append(value)

        elif opcode == 6:  # bdv - Divide A by 2^operand, store in B
            power = get_combo_value(operand, registers)
            registers['B'] = registers['A'] // (2 ** power)

        elif opcode == 7:  # cdv - Divide A by 2^operand, store in C
            power = get_combo_value(operand, registers)
            registers['C'] = registers['A'] // (2 ** power)

        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        # Move to the next instruction
        instruction_pointer += 2

    return output

# Run the program
output = run_program(registers, program)

# Output the result: Join output values with commas
result = "".join(map(str, output))
print("Program Output:", result)