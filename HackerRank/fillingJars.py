# Jesse Martinez
# Filling Jars

N, M = map( int, input().split() )

candies = 0
for operation in range( M ):
    start, end, candy = map( int, input().split() )
    candies += ( ( end - start ) + 1 ) * candy
print( candies // N )
