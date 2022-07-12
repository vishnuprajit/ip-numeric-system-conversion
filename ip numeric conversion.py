import re

# Welcome Note
print("IPv4 address - Format Converter")
print()
positions = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth")

# While Loop for getting and validationg 10 IP addresses
i = 0
while(i < 10):
    # Getting input (IP address) from user
    ip_address = input("Enter {} IP address: ".format(positions[i]))
    # Regex format of an IPv4 address
    ip_address_format = re.compile('([1-9][0-9]?[0-9]?)\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})')
    # Splitting the IPv4 address into an list of octets
    octets = list(map(int, ip_address.split(".")))

    # Checking whether each octet is with range of 0-255
    flag = True
    for octet in octets:
        if octet not in range(256):
            flag = False

    # Calculating Binary, Octal, Hexadecimal if Regex matches and all octets are inside the range(0-255).
    if ip_address_format.findall(ip_address) and flag:
        b = ".".join([bin(i)[2:] for i in octets])
        h = ".".join([hex(i)[2:] for i in octets])
        o = ".".join([oct(i)[2:] for i in octets])
        i += 1
    else:
        print("Invalid Format !!!")

    # print(ip_address + " " + b + " " + o + " " + h + "\n")
    # Appending the IPv4 address and their versions to the text file
    with open("conversion.txt", "a") as f:
        f.write(ip_address + ", " + b + ", " + o + ", " + h + "\n")
    
# Reading the text file and displaying the IPv4 address outputs.
with open("conversion.txt", "r") as f:
    for i in positions:
        addresses = f.readline()
        print("The {} IP address in Decimal, Binary, Octal, Hexadecimal is ".format(i) + addresses, end = "")