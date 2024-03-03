classA = [255,0,0,0]
classB = [255,255,0,0]
classC = [255,255,255,0]

def add_zeros_to_front(binary_str, desired_length):
    binary_list = [int(bit) for bit in binary_str]
    return [0] * (desired_length - len(binary_list)) + binary_list

def find_network_ip_address(classX, ip):
    result = [0]*4
    for i in range(0, len(classX)):
        result[i] = classX[i]&ip[i]
    print("Network IP Address: " + str(result))

    classXCopy = [0]*4
    result2 = [0]*4

    for i in range(0,len(classX)):
        if int(classX[i]) == 255:
            classXCopy[i] = 0
        elif int(classX[i]) == 0:
            classXCopy[i] = 255

        b = classXCopy[i]
        r = result[i]
        result2[i] = int(b)|int(r)
    print("Broadcast IP address: "+str(result2))

    result[3]+=1
    result2[3]-=1
    print("Usable Range of Host Addresses: ",result," to ",result2)
    

while True:
    user_input = input("Enter ip address: ")
    sections = user_input.split(".")
    sections = [int(i) for i in sections]

    binary = [0]*4

    for i in range(0,len(sections)):
        e = [0]*8
        b = bin(sections[i]).split('b')[1]
        e = add_zeros_to_front(b, 8)
        binary[i] = ("".join(str(e) for e in e))

    # Network IP Address is found using bitwise AND operation

    if sections[0] >= 0 and sections[0] <= 126:
        print("Class A Network")
        print("Default Network Mask: 255.0.0.0")
        print("# of Bits in Mask: 8")
        find_network_ip_address(classA, sections)
        print()
    if sections[0] >= 128 and sections[0] <= 191 and sections[1] <= 255:
        print("Class B Network")
        print("Default Network Mask: 255.255.0.0")
        print("# of Bits in Mask: 16")
        find_network_ip_address(classB, sections)
        print()
    if sections[0] >= 192 and sections[0] <= 233 and sections[1] <= 255 and sections[2] <= 255:
        print("Class C Network")
        print("Default Network Mask: 255.255.255.0")
        print("# of Bits in Mask: 24")
        find_network_ip_address(classC, sections)
        print()
    if sections[0] >= 224 and sections[0] <= 239:
        print("Class D Network (multicast)")
        print("Default Network Mask: not defined")
        print("# of Bits in Mask: 8")
        print("Broadcast IP Address for Network: Not defined")
        print("Usable range of Host Addresses: Not defined")
        print()
    if sections[0] >= 240 and sections[0] <= 255:
        print("Class E Network (reserved)")
        print("Default Network Mask: not defined")
        print("# of Bits in Mask: 8")
        print("Broadcast IP Address for Network: Not defined")
        print("Usable range of Host Addresses: Not defined")
        print()