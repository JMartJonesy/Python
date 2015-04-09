import math
def encryptionTable(n, e):
	for j in range(32, 127):
		letter = chr(j)
		cipherChr = squareAndMultiply(j, e, n)
		print(letter + " " + str(cipherChr))

def squareAndMultiply(a, r, p):
	if r == 0:
		return 1
	elif r == 1:
		return a
	elif r % 2 == 0:
		val = squareAndMultiply(a*a, r//2, p)
	else:
		val = a*squareAndMultiply(a*a, (r-1)//2, p)
	return (val % p)

if __name__ == "__main__":
	encryptionTable(int(input("Input n:")), int(input("Input e:")))
