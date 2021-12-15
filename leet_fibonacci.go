package main

/*
https://leetcode.com/problems/fibonacci-number/
*/

func main() {

	println(fib(5))

	/*
		0, 1, 1, 2, 3, 5, 8, 13
	*/
}

func fib(n int) int {
	if n == 0 {
		return 0
	}

	if n == 1 {
		return 1
	}

	fibo1 := 0
	fibo2 := 1
	var fibo3 int

	for i := 2; i <= n; i++ {
		fibo3 = fibo1 + fibo2

		fibo1 = fibo2
		fibo2 = fibo3
	}

	return fibo3
}
