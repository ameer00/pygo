 def fibonacci(n):
     """
     Calculates the nth Fibonacci number (0-indexed).

     Args:
         n: The index of the desired Fibonacci number (non-negative integer).

     Returns:
         The nth Fibonacci number.

     Raises:
         ValueError: If n is negative.
         TypeError: If n is not an integer.
     """
     if not isinstance(n, int):
         raise TypeError("Input must be an integer.")
     if n < 0:
         raise ValueError("Input must be a non-negative integer.")
     elif n == 0:
         return 0
     elif n == 1:
         return 1
     else:
         a, b = 0, 1
         for _ in range(2, n + 1):
             a, b = b, a + b
         return b