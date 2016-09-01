import sys, os


def find_items(credit, nitems, items):
	if nitems != len(items):
		print 'Error: number of items doesn\'t match with actual items in the list'
		sys.exit(1)

	for i in range(0, nitems-1):
		for j in range(i+1, nitems):
			if items[i] + items[j] == credit:
				return i+1, j+1


def main():
	if len(sys.argv) != 2:
		print "Usage: %s FILE" % sys.argv[0]
		sys.exit(1)

	if not os.path.exists(sys.argv[1]):
		print 'File not found'
		sys.exit(1)

	fo = open(sys.argv[1])
	test_cases = int(fo.readline()[:-1])
	for i in range(test_cases):
		credit = fo.readline()[:-1]
		nitems = fo.readline()[:-1]
		items = (fo.readline()).split()	
		items = map(int, items)
#		print credit, nitems, items
		item1, item2 = find_items(int(credit), int(nitems), items)
		print 'Case #%s: %s %s' % (i+1, item1, item2)
		

if __name__ == "__main__":
	main()
