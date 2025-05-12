 import math

 def square_root(n):
     """
     Calculates the square root of a non-negative number.

     Args:
         n: A non-negative number (integer or float).

     Returns:
         The square root of n.

     Raises:
         ValueError: If n is negative.
     """
     if n < 0:
         raise ValueError("Cannot calculate the square root of a negative number.")
     return math.sqrt(n)