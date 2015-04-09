# Jesse Martinez
# Gem Stones

checked = []
compositions = []
gemStones = 0
gems = int( input().strip() )

for gem in range( gems ):
	compositions.append( input().strip() )

for c in compositions[0]:
	if c in checked:
		continue
	else:
		checked.append( c )
		contains = True
		for composition in compositions[1:]:
			if not c in composition:
				contains = False
		if contains:
			gemStones += 1
print( gemStones )
