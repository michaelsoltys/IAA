// Tests for Algorithm 3 — Palindromes
// Label: alg:palindromes

package palindrome_test

import (
	"testing"

	palindrome "."
)

func TestIsPalindromeRacecar(t *testing.T) {
	if !palindrome.Alg("racecar") {
		t.Fail()
	}
}

func TestIsPalindromeAsdffdsa(t *testing.T) {
	if !palindrome.Alg("asdffdsa") {
		t.Fail()
	}
}

func TestIsPalindromeQwertyterwq(t *testing.T) {
	if palindrome.Alg("qwertyterwq") {
		t.Fail()
	}
}
