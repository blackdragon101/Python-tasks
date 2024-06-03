# This is a python program to convert bytes into megabytes and giga bytes.
units = int(input("""Enter the number in which you want to get bytes in
                 1.SI Units
                 2.Binary """))
bytes = int(input('Enter the bytes '))
if units == 1:
    mb = bytes/10**6
    gb = bytes/10**9
    print(f"The MBs are {mb} and the GBs are {gb}")
if units == 2:
    mega = bytes/1024**2
    giga = bytes/1024**3
    print(f"The MBs are {mega} and GBs are {giga}")





