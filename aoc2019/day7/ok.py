from itertools import permutations
nums = [3,8,1001,8,10,8,105,1,0,0,21,30,47,60,81,102,183,264,345,426,99999,3,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,102,4,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]

def do_op(i, inputs):
    # returns -1 if done, otherwise pointer to next instruction.
    args = []
    opstr = str(nums[i]).zfill(5)
    immediate = [bool(int(x)) for x in [opstr[2], opstr[1], opstr[0]]]
    op = int(opstr[3:])

    if op == 99:
        return -1

    # build input
    if op in [1, 2]:
        args = []
        for j in [1, 2]:
            if immediate[j-1]:
                args.append(nums[i+j])
            else:
                args.append(nums[nums[i+j]])
        args.append(nums[i+3])
    elif op == 3:  # build args for opcode 3 or 4
        args.append(nums[i + 1])
    elif op == 4:
        if immediate[0]:
            args.append(nums[i+1])
        else:
            args.append(nums[nums[i+1]])
    elif op in [5, 6]:
        if immediate[0]:
            args.append(nums[i+1])
        else:
            args.append(nums[nums[i+1]])
        if immediate[1]:
            args.append(nums[i+2])
        else:
            args.append(nums[nums[i+2]])
    elif op in [7, 8]:
        for j in [1, 2]:
            if immediate[j-1]:
                args.append(nums[i+j])
            else:
                args.append(nums[nums[i+j]])
        args.append(nums[i + 3])

    # execute
    if op == 1:
        dest = args[2]
        nums[dest] = args[0]+args[1]
        return i+4
    if op == 2:
        dest = args[2]
        nums[dest] = args[0]*args[1]
        return i+4
    if op == 3:
        nums[args[0]] = inputs.pop(0)
        return i+2
    if op == 4:
        #print("OUTPUT:", args[0])
        return [args[0]]
    if op == 5:
        # jump if true
        if bool(args[0]):
            return args[1]
        else:
            return i+3
    if op == 6:
        # jump if false
        if bool(args[0]):
            return i+3
        else:
            return args[1]
    if op == 7:
        # less than
        if args[0] < args[1]:
            nums[args[2]] = 1
        else:
            nums[args[2]] = 0
        return i+4
    if op == 8:
        #equal
        if args[0] == args[1]:
            nums[args[2]] = 1
        else:
            nums[args[2]] = 0
        return i+4

    print("BAD OPCODE", opstr)


def run(inputs):
    i = 0
    while i != -1:
        i = do_op(i, inputs)
        if type(i) is list:
            return i[0]

def run_phases(phases):
    sig = 0
    for phase in phases:
        #print('running with', sig, phase)
        sig = run([phase, sig])
        #print(sig)
    return sig

max_sig = 0
for p in permutations([0,1,2,3,4]):
    sig = run_phases(p)
    if sig > max_sig:
        max_sig = sig
print(max_sig)
