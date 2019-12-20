import copy
from itertools import permutations
prog = [3,8,1001,8,10,8,105,1,0,0,21,30,47,60,81,102,183,264,345,426,99999,3,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,102,4,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]

#prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

amplifiers = dict()

def reset_amps():
    global amplifiers
    amplifiers = {
        'A': copy.copy(prog),
        'B': copy.copy(prog),
        'C': copy.copy(prog),
        'D': copy.copy(prog),
        'E': copy.copy(prog),
    }
reset_amps()

"""
# am I reading this wrong..?
amplifiers = {
    'A': prog,
    'B': prog,
    'C': prog,
    'D': prog,
    'E': prog,
}
"""

def do_op(nums, i, inputs):
    # returns -1 if done, otherwise pointer to next instruction.
    #print("ptr is", i)
    args = []
    opstr = str(nums[i]).zfill(5)
    immediate = [bool(int(x)) for x in [opstr[2], opstr[1], opstr[0]]]
    op = int(opstr[3:])

    if op == 99:
        return -1, None

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
        return i+4, None
    if op == 2:
        dest = args[2]
        nums[dest] = args[0]*args[1]
        return i+4, None
    if op == 3:
        print("consuming input from", inputs)
        nums[args[0]] = inputs.pop(0)
        return i+2, None
    if op == 4:
        #print("OUTPUT:", args[0])
        return i+2, args[0]
    if op == 5:
        # jump if true
        if bool(args[0]):
            return args[1], None
        else:
            return i+3, None
    if op == 6:
        # jump if false
        if bool(args[0]):
            return i+3, None
        else:
            return args[1], None
    if op == 7:
        # less than
        if args[0] < args[1]:
            nums[args[2]] = 1
        else:
            nums[args[2]] = 0
        return i+4, None
    if op == 8:
        #equal
        if args[0] == args[1]:
            nums[args[2]] = 1
        else:
            nums[args[2]] = 0
        return i+4, None

    print("BAD OPCODE", opstr)


def run(ampName, ptr, inputs):
    while True:
        ptr, ret = do_op(amplifiers[ampName], ptr, inputs)
        if ptr == -1:
            # termination condition
            return None, None
        if ret is not None:
            # got an output. return it so the next amplifier can consume it
            print("output:", ret)
            return ptr, ret


def run_loop(phases):
    ampNames = ['A', 'B', 'C', 'D', 'E']
    sig = 0  # fed into A.
    ptrs = [0, 0, 0, 0, 0]
    last_sig = 0
    while sig is not None:
        for ampNum in range(5):
            inputs = []
            if len(phases):
                inputs.append(phases.pop(0))
            inputs.append(sig)
            #print("running", ampNames[ampNum], "with inputs", inputs)
            last_sig = sig
            ptr, sig = run(ampNames[ampNum], ptrs[ampNum], inputs)
            if ptr is None and sig is None:
                # terminated (99)
                return last_sig
            ptrs[ampNum] = ptr
            #print("sig", sig)

max_sig = 0
for p in permutations([9,8,7,6,5]):
    print(p)
    sig = run_loop(list(p))
    if sig > max_sig:
        max_sig = sig
    reset_amps()
print("max sig was:", max_sig)
