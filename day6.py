def find_start_of_packet(signal: str) -> int:
    return find_unique_chunk_of_size(signal, 4)


def find_start_of_message(signal: str) -> int:
    return find_unique_chunk_of_size(signal, 14)


def find_unique_chunk_of_size(signal: str, size: int) -> int:
    for i in range(0, len(signal) - size):
        chunk_start = i
        chunk_end = i + size
        chunk = signal[chunk_start:chunk_end]
        if len(set(chunk)) == size:
            return chunk_end


signal = ""
with open("input/day6_input.txt") as f:
    signal = f.read().strip()

packet_start_index = find_start_of_packet(signal)
message_start_index = find_start_of_message(signal)

print(f"Packet start index: {packet_start_index}")
print(f"Message start index: {message_start_index}")

