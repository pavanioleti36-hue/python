str = "pavanioleti"
f = {}
for x in str:
    if x in f:
        f[x] += 1
    else:
        f[x] = 1
for key in f:
    print(key, ":", f[key])