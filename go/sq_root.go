package mathops

import "math"

// SquareRoot calculates the square root of a non-negative float64 number.
// It returns NaN for negative inputs.
func SquareRoot(n float64) float64 {
	return math.Sqrt(n)
}