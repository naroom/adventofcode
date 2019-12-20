import copy

def run(nums):
    for i in range(len(nums) // 4):
        #print(nums[:40])
        op = nums[i*4]
        if op == 99:
            break
        a = nums[nums[i*4+1]]
        b = nums[nums[i*4+2]]
        loc = nums[i*4+3]
        if op == 1:
            #print("pos: {} op: {}+{} to: {}".format(i*4, a, b, loc))
            nums[loc] = a+b
        if op == 2:
            #print("pos: {} op: {}*{} to: {}".format(i*4, a, b, loc))
            nums[loc] = a*b
    return nums

ls = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,143,0,99,2,14,0,0"""
ls = ls.replace(',', '\n')
p = [int(n) for n in ls.split('\n') if n.strip()]

for in1 in range(100):
    for in2 in range(100):
        p[1] = in1
        p[2] = in2
        q = run(copy.deepcopy(p))
        print(in1, in2, q[0])
        if q[0] == 19690720:
            print(100*in1+in2)
            print(in1,in2)
            break

#p = [2,4,4,5,99,0]
out = run(p)