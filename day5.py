from collections import deque
crate_lines = []
with open("input/day5_input_crates.txt") as f:
    crate_lines = f.readlines()

crate_lines = crate_lines[:-1]


stacks = []
stack_count = 9
for i in range(0, stack_count):
    stacks.append(deque([]))


for row in reversed(crate_lines):
    for i in range(0, stack_count):
        crate_label = row[(4 * i) + 1]
        if crate_label != " ":
            stacks[i].append(crate_label)

instructions = []
with open("input/day5_input_instructions.txt") as f:
    instructions = f.readlines()

instruction_tuples = []
for line in instructions:
    instruction_pieces = line.split(" ")
    instruction_tuples.append(
        (
            int(instruction_pieces[1]),
            int(instruction_pieces[3]),
            int(instruction_pieces[5]),
        )
    )
    
for instruction in instruction_tuples:
    count = instruction[0]
    origin_stack_index = instruction[1] - 1
    destination_stack_index = instruction[2] - 1
    
    intermediate_stack = deque()
    for i in range(0, count):
        #stacks[destination_stack_index].append(stacks[origin_stack_index].pop())
        intermediate_stack.append(stacks[origin_stack_index].pop())
    
    for i in range(0, count):
        stacks[destination_stack_index].append(intermediate_stack.pop())


for i in range(0, stack_count):
    print(f"Top item of stack {i + 1}: {stacks[i].pop()}")