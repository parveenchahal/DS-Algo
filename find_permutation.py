# https://www.interviewbit.com/problems/find-permutation/

def find_permutation(s, n):
    small, large = 1, n
    result = []
    for x in s:
        if x == 'I':
            result.append(small)
            small += 1
        else:
            result.append(large)
            large -= 1
    result.append(small)
    return result
        

def find_permutation2(s, n):
    result = []
    count = 1
    d_count = 0
    i = 0
    if s[0] == 'I':
        result.append(count)
        count += 1
    else:
        while(i < n - 1 and s[i] != 'I'):
            d_count += 1
            i += 1
        count += d_count + 1
        t = count - 1
        result.append(t)
        t -= 1
        while(d_count > 0):
            result.append(t)
            t -= 1
            d_count -= 1

    while(i < n - 1):
        if s[i] == 'I' and(i >= n - 2 or s[i + 1] == 'I'):
            result.append(count)
            count += 1
            i += 1
        else:
            i += 1
            while(i < n - 1 and s[i] != 'I'):
                d_count += 1
                i += 1
            t = count + d_count
            result.append(t)
            count += 1
            t -= 1
            while(d_count > 0):
                result.append(t)
                count += 1
                t -= 1
                d_count -= 1
    return result

r = find_permutation("III", 4)
print(r)

r = find_permutation("DDD", 4)
print(r)

r = find_permutation("ID", 3)
print(r)

r = find_permutation("IIDDI", 6)
print(r)
