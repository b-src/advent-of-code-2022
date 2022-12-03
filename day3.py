class Rucksack:
    def __init__(self, contents):
        self.contents = contents.strip()
        limit = int(len(contents) / 2)
        self.compartment1 = contents[0:limit]
        self.compartment2 = contents[limit:]
    
        self.common_elements = set(self.compartment1) & set(self.compartment2)
        self.calculate_total_priority()
    
    def calculate_total_priority(self):
        priority = 0
        if self.common_elements:
            for char in self.common_elements:
                priority += self.calculate_priority(char)
        
        self.priority = priority

    def calculate_priority(self, char: str):
        # ascii value of 'a': 97
        # ascii value of 'A': 65
        if char.isupper():
            return (ord(char) - (65 - 27))
        else:
            return (ord(char) - 96)


class RucksackGroup:
    def __init__(self, rucksacks: list[Rucksack]):
        self.rucksacks = rucksacks
        self.common_element = set(rucksacks[0].contents) & set(rucksacks[1].contents) & set(rucksacks[2].contents)
        self.priority = rucksacks[0].calculate_priority(self.common_element.pop())
        
    
rucksacks = []

with open("input/day3_input.txt") as f:
    rucksacks = f.readlines()

rucksacks = [Rucksack(contents) for contents in rucksacks]
total_priority = 0
for rucksack in rucksacks:
    total_priority += rucksack.priority

rucksack_groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
groups = [RucksackGroup(group) for group in rucksack_groups]
rucksack_group_total_priority = 0
for group in groups:
    rucksack_group_total_priority += group.priority

print(f"Total priority: {total_priority}")
print(f"Total group priority: {rucksack_group_total_priority}")