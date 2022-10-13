x =input("please enter your sentence here :").lower()
z = x.split()
for y, r in enumerate(z):
    a = ['a','i','u','e','o']
    if r[0] in a:
        z[y] = z[y] + "ay"
    else:
        xx = False
        for zz, rr in enumerate(r):
            if rr in a:
                z[y]=r[zz:] + r[:zz] + "ay"
                xx = True
                break
        if (xx == False):
            z[y] = r[zz:] + r[:zz] + "ay"
xxx =" ".join(z)
print(xxx)
