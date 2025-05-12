package mathops

// Fibonacci calculates the nth Fibonacci number iteratively.
// Note: Returns 0 for n <= 0. For large n, consider using big.Int.
func Fibonacci(n int) int {
	if n <= 0 {
		return 0
	}
	a, b := 0, 1
	for i := 1; i < n; i++ {
		a, b = b, a+b
	}
	return b
}