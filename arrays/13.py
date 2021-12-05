def twoSum(n,t):
    m={}
    for i,v in enumerate(n):
        diff = t-n[i]
        if diff in m:
            return [m[diff], i]
        m[v]= i

print(twoSum([5,9,7],16))
