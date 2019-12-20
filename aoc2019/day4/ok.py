
def check_nondecreasing(si):
    return all(int(si[i-1]) <= int(si[i]) for i in range(1,6))


def check_no_run_doubles(si):
    mp = [si[i-1] == si[i] for i in range(1,6)]  # "matches previous"
    if not any(mp):
        return False
    #edges
    if mp[0] == 1 and mp[1] == 0:
        return True
    if mp[4] == 1 and mp[3] == 0:
        return True
    ok = [1 for i in range(1,4) if (mp[i] == 1 and mp[i-1] == 0 and mp[i+1] == 0)]
    return ok

print(check_nondecreasing('123456'), 'true')
print(check_nondecreasing('100001'), 'false')
print("")
print(check_no_run_doubles('111166'), 'true')
print(check_no_run_doubles('123566'), 'true')
print(check_no_run_doubles('113596'), 'true')
print(check_no_run_doubles('113455'), 'true')
print(check_no_run_doubles('112244'), 'true')
print(check_no_run_doubles('111455'), 'false')
print(check_no_run_doubles('125556'), 'false')
print(check_no_run_doubles('123456'), 'false')

count = 0
for i in range(307237, 769058):
    si = str(i)
    if check_nondecreasing(si) and check_no_run_doubles(si):
        count += 1


print(count)