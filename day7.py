from collections import deque

class Node:
    def __init__(self, name: str, is_dir: bool, parent):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        if is_dir:
            self.children = {}
    
    def set_size(self, size: int):
        self.size = size
    
    def add_child(self, child_node):
        if not self.is_dir:
            raise Exception("Cannot add child to files")
        else:
            self.children[child_node.name] = child_node


def build_filesystem_tree(input_lines: list[str]):
    root_node = Node("/", True, None)
    current_node = root_node

    for line in input_lines:
        words = line.strip().split(" ")
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "/":
                    # do nothing, root node is handled initially
                    pass
                elif words[2] == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.children[words[2]]
            elif words[1] == "ls":
                # do nothing, next actions will describe node
                pass
        elif words[0] == "dir":
            current_node.add_child(
                Node(name=words[1], is_dir=True, parent=current_node)
            )
        else:
            file_node = Node(name=words[1], is_dir=False, parent=current_node)
            file_node.set_size(int(words[0]))
            current_node.add_child(file_node)
    
    return root_node


def set_directory_sizes(root_node: Node):
    total_size = 0

    for child_name in root_node.children.keys():
        if root_node.children[child_name].is_dir:
            set_directory_sizes(root_node.children[child_name])
        total_size += root_node.children[child_name].size

    root_node.set_size(total_size)


def get_all_directories_under_size(root_node: Node, threshold: int):
    directories = []
    directory_queue = deque()
    directory_queue.append(root_node)
    
    while directory_queue:
        current_node = directory_queue.popleft()
        for child_name in current_node.children.keys():
            child = current_node.children[child_name]
            if child.is_dir:
                directory_queue.append(child)

        if current_node.size <= threshold:
            directories.append(current_node)
    
    return directories


def get_all_directories_by_size(root_node: Node):
    directories = []
    directory_queue = deque()
    directory_queue.append(root_node)
    
    while directory_queue:
        current_node = directory_queue.popleft()
        for child_name in current_node.children.keys():
            child = current_node.children[child_name]
            if child.is_dir:
                directory_queue.append(child)

        directories.append(current_node)

    directories.sort(key=lambda directory: directory.size)
    
    return directories


input_lines = []

with open("input/day7_input.txt") as f:
    input_lines = f.readlines()
    
filesystem_root_node = build_filesystem_tree(input_lines)
set_directory_sizes(filesystem_root_node)

directories_of_interest = get_all_directories_under_size(filesystem_root_node, 100000)

total_size = 0
for directory in directories_of_interest:
    total_size += directory.size

print(f"Total size of dirs <= 100000 (bits?): {total_size}")

directories_by_size = get_all_directories_by_size(filesystem_root_node)

total_space = 70000000
space_needed_for_update = 30000000
free_space = total_space - filesystem_root_node.size
space_needed_to_free = space_needed_for_update - free_space

for directory in directories_by_size:
    if directory.size < space_needed_to_free:
        continue
    
    print(f"Smallest deleteable directory: {directory.name} with size {directory.size}")
    break
