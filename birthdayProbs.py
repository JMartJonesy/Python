import math
def probs(start, finish):
	tot = 1
	for i in range(1, finish+1):
		tot *= (1-((i - 1)/365))	
		if(i >= start):
			print(str(i) + " val-" + str(tot))

def approximation(finish):
	for i in range(1, finish+1):
		if i >= 15:
			tot = 0
			for j in range(1, i-1):
				tot+= j
			tot = math.pow(math.e,(-1)*(tot/365))
			print(str(i) + ":" + str(tot))

if __name__ == "__main__":
	start = int(input())
	finish = int(input())
	probs(start, finish)
	approximation(finish)
