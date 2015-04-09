import sys

def main():
	found = False
	origVal = int( sys.argv[1] )
	ringVal = int( sys.argv[2] )
	findVal = 0

	for i in range( ringVal ):
		if ( ( i * origVal ) % ringVal ) == 1:
			findVal = i
			found = True
			break
	
	if found:
		print( "Multiplicative Inverse of " + str( origVal ) + " is " +                         str( findVal  ) )
	else:
		print("No Multiplicative Inverse found for " + str( origVal ) )

main()
