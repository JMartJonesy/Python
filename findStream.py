import sys

def main():
	plainText = list(sys.argv[1].rstrip())
	cipherText = list(sys.argv[2].rstrip())
	keyStream = ""

	for index in range( 0, len(plainText) ):
		if index != 0 and (( index % 4 ) == 0):
			keyStream += " "
		if ((( int(plainText[index]) + 1 ) % 2 ) == int(cipherText[index] )):
			keyStream += "1"
		else:
			keyStream += "0"
	
	print( keyStream )

main()
