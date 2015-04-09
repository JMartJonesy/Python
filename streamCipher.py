import sys

def main():
	decryption = False
	text = list(sys.argv[2].rstrip())
	keyStream = list(sys.argv[3].rstrip())

	if( sys.argv[1] == "-d"):
		decryption = True
	
	if( decryption ):
		for index in range( 0, len(text) ):
			textChar = ord(text[index]) - 97
			keyChar = ord(keyStream[index]) - 97

			if( text[index] != " "):
				text[index] = chr(((textChar - keyChar) % 26) + 97)
		print("Decrypted: " + "".join(text))

main()
