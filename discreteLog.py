import math

def findX(base, val, n):
	answer = 0
	for i in range(1, n):
		tot = math.pow(base, i) % n
		if tot == val:
			answer = i
	if answer == 0:
		print("Not Defined")
	else:
		print(str(answer))

if __name__ == "__main__":
	base = int(input("input base:"))
	val = int(input("input val:"))
	n = int(input("input n:"))
	findX(base, val, n)
