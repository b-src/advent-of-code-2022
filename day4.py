class AssignmentPair:
    def __init__(self, sections: str):
        assignments = sections.split(",")
        range_a_limits = assignments[0].split("-")
        range_b_limits = assignments[1].split("-")
        range_a = range(int(range_a_limits[0]), int(range_a_limits[1]) + 1)
        range_b = range(int(range_b_limits[0]), int(range_b_limits[1]) + 1)
        
        self.a_sections = set(range_a)
        self.b_sections = set(range_b)
    
    def is_subset(self):
        return self.a_sections.issubset(self.b_sections) or self.b_sections.issubset(self.a_sections)
    
    def has_overlap(self):
        return bool(self.a_sections.intersection(self.b_sections))


assignments = []

with open("input/day4_input.txt") as f:
    assignments = f.readlines()

assignment_pairs = [AssignmentPair(assignment) for assignment in assignments]

subset_count = 0
overlap_count = 0

for pair in assignment_pairs:
    if pair.is_subset():
        subset_count += 1
    if pair.has_overlap():
        overlap_count += 1

print(f"Subset count: {subset_count}")
print(f"Overlap count: {overlap_count}")