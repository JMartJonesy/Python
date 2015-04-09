import math
import random

primes = []

#Parses a txt file with all prime between 100000 and 110000
def parsePrimes(fileName):
	for line in open(fileName):
		line = line.strip().split("   ")
		for prime in line:
			primes.append(int(prime.strip()))

#runs the Miller-Rabin theorem from 2 to the p(prime number being tested) - 2
def runMiller(p, prime):
	count = 0
	u, r = 0, p-1
	#factor out all powers of 2
	while r % 2 == 0:
		u += 1
		r //= 2
	#test all a values from 2 to p-2
	for a in range(2, p - 2):
		#if answer is not correct add 1 to count
		if millerHelper(u, r, p, a) != prime:
			count += 1
	return count

#test a value
def millerHelper(u, r, p, a):
	#take a^r mod p
	t = squareAndMultiply(a, r, p)
	#if a^r mod p is 1 then p is likely prime
	if t == 1:
		return True
	#add back in the squares we removed an stored in u
	while u > 0:
		#if we get to a p-1 then p is likely prime
		if t == (p-1):
			return True
		#square t and decrement u 
		t, u = squareAndMultiply(t, 2, p), u-1
	return False

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

#find error percentages for each odd between 100000 and 110000
if __name__ == "__main__":
	parsePrimes("primesGood.txt")
	maxError = 0
	for p in range(100001, 110001, 2):
		prime = p in primes
		count = runMiller(p, prime)
		errorPerc = count / (p-3)
		if maxError < errorPerc:
			maxError = errorPerc
		if prime:
			print(str(p) + " is prime with an error percentage of " + str(errorPerc))
		else:
			print(str(p) + " is composite with an error percentage of " + str(errorPerc))
	print("Max Error Percentage:" + str(maxError))
