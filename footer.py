

passed = True
title = "dump test"
test = print
args = list()  # type: List[Any]
resf = 0.0.hex()
resF = None

# class tree
passed = issubclass(Float, binary64)
if not passed:
    print("Float is not subclass of binary64", file=sys.stderr)

inf = ["Nan", "INF", "-inf", "infINIty"]
pconstr = []
for ival in inf:
    pval = Float(ival).hex() == float(ival).hex()
    pconstr.append(pval)
    if not pval:
        print("invalid constructor", ival, Float(ival).hex(), float(ival).hex(),
              sep="\t", file=sys.stderr)
for i in range(1000):
    base = str(random.random())
    exps = [random.randint(-128, 128), random.randint(-2**11, -128), random.randint(128, 2**10)]
    pos = list(map(lambda x: base + "e" + str(x), exps))
    neg = list(map(lambda x: "-" + x, pos))
    vals = pos + neg
    for val in vals:
        pval = Float(val).hex() == float(val).hex()
        pconstr.append(pval)
        if not pval:
            print("invalid constructor", val, Float(val).hex(), float(val).hex(),
                  sep="\t", file=sys.stderr)
passed = passed and all(pconstr)

if passed:
    print("YES")
else:
    print("NO")
