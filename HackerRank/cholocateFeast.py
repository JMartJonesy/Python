# Jesse Martinez
# Chocolate Feast

for testCase in range( int( input().strip() ) ):
	N, C, M = map( int, input().split() )
	bought = ( N // C )
	free = ( bought // M )
	extras = ( ( bought - ( free * M ) ) + free ) // M
	print( bought + free + extras )
