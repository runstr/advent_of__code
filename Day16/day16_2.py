from Tools import *
day = path.dirname(__file__)[-2:]
input_filename = __file__[:-10]+"input.txt"
test_input1_filename = __file__[:-10]+"test_input.txt"
import math

def decode_packet(packet, while_loop , version_list):
    uncoded_packet = packet
    packets = []
    while len(set(uncoded_packet)) != 1 and len(uncoded_packet) != 0:
        version = int(uncoded_packet[:3], 2)
        version_list[0] += version
        packet_type = int(uncoded_packet[3:6], 2)
        uncoded_packet = uncoded_packet[6:]
        full_packet = {"version": version, "type": packet_type}
        if packet_type == 4:
            packet_done = False
            literal = ""
            while not packet_done:
                if uncoded_packet[0] == "0":
                    packet_done = True
                literal += uncoded_packet[1:5]
                uncoded_packet = uncoded_packet[5:]
            full_packet["packet"] = int(literal, 2)
        else:
            length_id = int(uncoded_packet[0], 2)
            uncoded_packet = uncoded_packet[1:]
            if length_id == 1:
                new_packet = []
                num_packets = int(uncoded_packet[0:11], 2)
                new_uncoded = uncoded_packet[11:]
                for _ in range(num_packets):
                    new_packets, new_uncoded = decode_packet(new_uncoded, while_loop=False, version_list=version_list)
                    new_packet.append(new_packets)
                uncoded_packet = new_uncoded
            else:
                length = int(uncoded_packet[0:15], 2)
                uncoded_packet = uncoded_packet[15:]
                new_packet = decode_packet(uncoded_packet[:length], while_loop=True, version_list=version_list)
                uncoded_packet = uncoded_packet[length:]
            full_packet["packet"] = new_packet
        packets.append(full_packet)
        if not while_loop:
            return packets, uncoded_packet
    return packets

def calculate_packet(packets):
    values = []
    if type(packets) == list:
        packets = packets[0]
    packet_type = packets["type"]
    if packet_type == 4:
        return packets["packet"]
    elif packet_type == 0:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return sum(values)
    elif packet_type == 1:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return math.prod(values)
    elif packet_type == 2:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return min(values)
    elif packet_type == 3:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return max(values)
    elif packet_type == 5:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return int(values[0]>values[1])
    elif packet_type == 6:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return int(values[0]<values[1])
    elif packet_type == 7:
        for packet in packets["packet"]:
            values.append(calculate_packet(packet))
        return int(values[0]==values[1])

def execution():
    input_full = read_input_as_line(input_filename)[0]
    version_list = [0]
    uncoded_binary = bin(int(input_full, 16))[2:].zfill(len(input_full) * 4)
    decoded_packet = decode_packet(uncoded_binary, while_loop=True, version_list=version_list)
    answer = calculate_packet(decoded_packet)
    print("Answer to day {} task two is: {}".format(day, answer))
