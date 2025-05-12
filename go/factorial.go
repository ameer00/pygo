package mathops

// Factorial calculates the factorial of a non-negative integer n (n!).
// Note: Returns 1 for n = 0. Returns 0 for negative n (as factorial is undefined).
// For large n, consider using big.Int.
func Factorial(n int) int {
	if n < 0 {
		return 0 // Or handle as an error
	}
	if n == 0 {
		return 1
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result
}