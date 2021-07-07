import sys
if len(sys.argv) < 4:
    print("USAGE: color_palette_shifter.py <input file> <output file> <shift size>")
    print("ERROR:")
    if len(sys.argv) < 3:
        if len(sys.argv) < 2:
            sys.exit("    Input color file is not specified")
        sys.exit("    Output color file is not specified")
    sys.exit("    Left cyclic shift size is not specified")

def cyclic_lshift(line, shift_size=2):
    ll = list(line)
    #print(ll)
    for i in range(shift_size):
        ll.append(ll.pop(0))
        #print(ll)
    result = ''
    for i in ll:
        result += i
    return result

stop_line = '#Other theme attributes'
val_len = 6
shift_size = int(sys.argv[3])

with open(sys.argv[1]) as ifile:
    with open(sys.argv[2], 'w') as ofile:
        accumulator = ''
        flag = True
        for line in ifile:
            if line.startswith(stop_line):
                flag = False
            if '=' in line and flag is True:
                iao_pos = line.find('=') + 1
                line = line[:iao_pos] + cyclic_lshift(
                                                    line[iao_pos:iao_pos + val_len],
                                                    shift_size
                                                    )
               #print(line)
            accumulator += (line + '\n')
        ofile.write(accumulator)

