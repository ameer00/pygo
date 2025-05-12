package mathops

import "errors"

// Divide takes two float64 numbers and returns their quotient (a / b).
// It returns an error if the divisor (b) is zero.
func Divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("division by zero is not allowed")
	}
	return a / b, nil
}