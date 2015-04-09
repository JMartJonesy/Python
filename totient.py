import math

primes = []

#Parses a txt file with all prime between 100000 and 110000
def parsePrimes(fileName):
	for line in open(fileName):
		line = line.strip().split(" ")
		for prime in line:
			if prime.strip().isdigit():
				primes.append(int(prime.strip()))

def findFactors(n):
	index = 0
	factors = []
	while primes[index] <= n:
		if n % primes[index] == 0:
			n //= primes[index]
			factors.append(primes[index])
		else:
			index += 1
	return factors

def findTotient(n, factors = []):
	if n in primes:
		return n-1
	else:
		totients = []
		if len(factors) == 0:
			factors = findFactors(n)
		while len(factors) > 0:
			factor = factors[0]
			count = factors.count(factor)
			totients.append(math.pow(factor,count) - math.pow(factor, count - 1))
			while len(factors) > 0 and factors[0] == factor:
				factors.remove(factor)
	ans = 1
	for value in totients:
		ans *= value
	return int(ans)

if __name__ == "__main__":
	parsePrimes("primes1.txt")
	n = int(input("Input prime:"))
	print("Factors:" + str(findFactors(n)))
	print("Totient:" + str(findTotient(n)))
