import sys

def main():
	count = 0
	counts = [0] * 26
	
	for line in open( sys.argv[1] ):
		for charage in line.strip():
			count += 1
			counts[ ord( charage ) - 97 ] += 1
	
	for index in range( len( counts ) ):
		print( counts[index] )
		print( chr( index + 97 ) + " " + str(counts[index] / count * 100) + "%"  )

main()
