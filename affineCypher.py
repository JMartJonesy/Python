import sys
from fractions import gcd

def main():
	a = 7
	b = 22
	aInverse = 0
	found = False
	clearText = ""

	for i in range(26):
		if ((i * a) % 26) == 1:
			aInverse = i
			break

	for line in open(sys.argv[1]):
		for charage in line.strip():
			charVal = ord( charage ) - 97
			charVal = charVal - b
			charVal = charVal * aInverse
			charVal = charVal % 26
			clearText += (chr(int(charVal + 97)))
	
	print( clearText )

main()
