import sys, os.path


def main():
	if len(sys.argv) != 2:
		print 'Usage: %s file' % sys.argv[0]
		sys.exit(1)

	if not os.path.exists(sys.argv[1]):
		print 'File not found'
		sys.exit(1)

	try:
		f = open(sys.argv[1])
		cases = int(f.readline()[:-1])
		c = 1
		for line in f:
			words = line.split()
			words.reverse()
			print 'Case #%s: %s' % (c, ' '.join(words))
			c += 1

	except IOError as e:
		print "I/O error(%s): %s" % (e.errno, e.strerror)
		sys.exit(1)
	except:
		print 'Unexpected error', sys.exec_info()
	
	

if __name__ == "__main__":
	main()
