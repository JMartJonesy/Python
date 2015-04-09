import os.path
import sys
from sys import argv

if( len(argv) == 4 ):
	file_name = argv[1]
	mode = argv[2]
	offset = argv[3]
elif( len(argv) == 3 ):
	file_name = argv[1]
	mode = argv[2]
elif( len(argv) == 2 ):
	file_name = argv[1]
	mode = 'e'
else:
	print("Try Again")
	sys.exit(0)

if( leng(argv) != 4 ):
	offset = int( input("Input ascii offset:") )

if( mode == 'e' ):
	writeFile = open('encrypted-' + file_name, 'w')
else:
	writeFile = open('decrypted-' + file_name, 'w')
	offset = offset * -1

readFile = open(file_name)

if( mode == 'e' ):
	print("Encrypting File:", file_name)
else:
	print("Decrypting File:", file_name)

for char in readFile.read():
	if( 32 <= ord( char ) <= 127 ):
		writeFile.write( chr( ord( char ) + offset ) )
	else:
		writeFile.write( char )

writeFile.close()
readFile.close()

if( mode =='e' ):
	print("Encryption Finished")
else:
	print("Decryption Finished")
