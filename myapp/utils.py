"""Small utility functions to demonstrate testing and linting."""
from typing import Union




def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
"""Return the sum of a and b."""
return a + b




def divide(a: Union[int, float], b: Union[int, float]) -> float:
"""Divide a by b. Raises ValueError if b == 0."""
if b == 0:
raise ValueError("divider must not be zero")
return a / b