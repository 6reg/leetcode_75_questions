def ts(n, t):
    hm={}
    for i,v in enumerate(n):
        d = t - n[i]
        if d in hm:
            return [hm[d], i]
        hm[v] = i

print(ts([2, 7, 9], 9))
