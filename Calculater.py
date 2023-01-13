a=int(float(input("import Number 1 .....")))
b=int(float(input("import Number 2 ......")))
c=(input("type A for add and B for subtract and C for product  and D for divide  and E for get reminder    --"))
if c == "A":
    e=float((a+b))
if c == "B":
    e=float((a-b))
if c == "C":
    e=float((a*b))
if c == "D":
    e=float((a/b))
if c == "E":
    e=float((a%b))
if c == "a":
    e=float((a+b))
if c == "b":
    e=float((a-b))
if c == "c":
    e=float((a*b))
if c == "d":
    e=float((a/b))
if c == "e":
    e=float((a%b))
else:
    print("")
print(e)
