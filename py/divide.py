 def divide(a, b):
     """
     Returns the result of dividing the first number by the second.

     Args:
         a: The numerator.
         b: The denominator.

     Returns:
         The result of a divided by b.

     Raises:
         ValueError: If the denominator (b) is zero.
     """
     if b == 0:
         raise ValueError("Cannot divide by zero!")
     return a / b