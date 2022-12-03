lines = []

with open("input/day1_input.txt") as f:
    lines = f.readlines()

current_calories = 0
total_calories_per_elf = []
for line in lines:
    if line != '\n':
        current_calories += int(line)
    else:
        total_calories_per_elf.append(current_calories)
        current_calories = 0

total_calories_per_elf.sort(reverse=True)

print(f"Most calories: {total_calories_per_elf[0]}")
print(f"Second most calories: {total_calories_per_elf[1]}")
print(f"Third most calories: {total_calories_per_elf[2]}")

print(f"Total calories for top 3: {total_calories_per_elf[0] + total_calories_per_elf[1] + total_calories_per_elf[2]}")