import math
from totient import *
def findAllOrders(n):
	count = 0
	for i in range(1, n):
		if findOrder(i,n) == (n-1):
			count += 1
			print("ord(" + str(i) + ") = " + str(findOrder(i, n)) + " <- Generator" )
		print("ord(" + str(i) + ") = " + str(findOrder(i, n)))
	print("There are " + str(count) + " generators for " + str(n))

def findOrder(a, n):
	for i in range(1, n):
		val = squareAndMultiply(a, i, n)
		if val == 1:
			return i
	return 0

def squareAndMultiply(a, r, p):
	binaryExponent = []
	
	#create binary representation of r and store in a list
	while r != 0:
		binaryExponent.append(r % 2)
		r = r // 2
	binaryExponent.reverse()
	ans = 1

	#Square and Multiply modulo p in each step
	for bit in binaryExponent:
		ans = (ans*ans) % p
		if bit == 1:
			ans = (ans*a) % p
	return ans

if __name__ == "__main__":
	n = int(input("Input n:"))
	findAllOrders(n)
	parePrimes("primes1.txt")
	print("Fast Calcuation: # of Generators is ")
