// Algorithm 6, Page 10 — Ulam's Algorithm
// Label: alg:ulam
// An Introduction to the Analysis of Algorithms (4th Edition)
//
// Computes the Ulam (3n+1) trajectory until reaching the cycle 4,2,1.

package ulam

// Alg pre-condition: a > 0
func Alg(a int) {
	x := a

	lastValues := make([]int, 3)

	for lastValues[0] != 4 || lastValues[1] != 2 || lastValues[2] != 1 {
		if x%2 == 0 {
			x = x / 2
		} else {
			x = 3*x + 1
		}

		lastValues = append(lastValues[1:], x)
	}
}
