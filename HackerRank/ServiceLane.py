# Jesse Martinez
# Service Lane 
""" Slow but less lines
N, T = map( int, input().split() )
widths = input().split()

for test in range( T ):
    start, end = map( int, input().split() )
        print( str( min( widths[start:( end + 1 )] ) ) )
"""
import sys

cars = [1,2,3]
NT = sys.stdin.readline().split()
T = int( NT.pop() )
widths = sys.stdin.readline().split() 
for test in range( T ):
    testCase = sys.stdin.readline().split()
        width = int( min( widths[int( testCase[0] ):int( testCase[1] ) + 1] ) )
	    print( str( min( cars, key=lambda  car:abs( width - car ) ) ) ) 
