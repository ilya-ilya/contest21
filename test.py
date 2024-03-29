"""Module with Float class."""
from typing import *
from abc import abstractmethod
from numbers import Real
import sys
import random


class binary64(Real):
    """ABC for Floats."""

    @abstractmethod
    def as_integer_ratio(self) -> Tuple[int, int]:
        """Return a pair of integers whose ratio is exactly equal to the original float."""
        pass

    @abstractmethod
    def is_integer(self) -> bool:
        """Return True if the float instance is finite with integral value."""
        pass

    @abstractmethod
    def hex(self) -> str:
        """Return a representation of a floating-point number as a hexadecimal string."""
        pass

    @classmethod
    @abstractmethod
    def fromhex(cls, s: str) -> "binary64":
        """Class method to return the float represented by a hexadecimal string s."""
        pass


binary64.register(float)


Float = float


class A:
    pass


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
