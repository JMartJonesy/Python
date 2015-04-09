import sys

def main():
	shift = int( input("Input shift value:") )
	shiftString = ""

	for line in open( sys.argv[1] ):
		for charage in line.strip():
			shiftloc = ( ord( charage ) - 97 - shift ) % 26
			shiftString += chr( shiftloc + 97 )
	
	print( shiftString )

main()
