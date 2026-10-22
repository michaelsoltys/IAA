// Algorithm 3, Page 7 — Palindromes
// Label: alg:palindromes
// An Introduction to the Analysis of Algorithms (4th Edition)
//
// Checks whether a given string is a palindrome.

package palindrome

// Alg returns whether a given string word is a palindrome.
func Alg(word string) bool {
	n := len(word) - 1
	for i := 0; i <= len(word)/2; i++ {
		if word[i] != word[n-i] {
			return false
		}
	}
	return true
}
