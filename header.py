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


