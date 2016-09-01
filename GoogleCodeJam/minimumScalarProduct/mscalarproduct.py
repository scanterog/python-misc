"""
The minimum sum of products occurs only when you multiply a smaller number in vector 1 with the larger number in vector 2 and add all such occurrences. 
"""

def main():
	cases = int(raw_input())
	for case in range(cases):
		nitems = int(raw_input())
		v1 = map(int, str(raw_input()).split())
		v2 = map(int, str(raw_input()).split())
		v1o = sorted(v1)
		v2o = sorted(v2, reverse=True)
		scalar = 0
		for i in range(nitems):
			scalar += int(v1o[i]) * int(v2o[i])
		print "Case #%s: %s" % (case + 1, scalar)
	

if __name__ == "__main__":
	main()
