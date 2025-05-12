 def factorial(n):
     """
     Calculates the factorial of a non-negative integer.

     Args:
         n: A non-negative integer.

     Returns:
         The factorial of n (n!).

     Raises:
         ValueError: If n is negative.
         TypeError: If n is not an integer.
     """
     if not isinstance(n, int):
         raise TypeError("Input must be an integer.")
     if n < 0:
         raise ValueError("Factorial is not defined for negative numbers.")
     elif n == 0:
         return 1
     else:
         result = 1
         for i in range(1, n + 1):
             result *= i
         return result