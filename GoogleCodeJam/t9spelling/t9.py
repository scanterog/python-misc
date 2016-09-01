import sys

def translate(caseno, msg):
	d = {'0': [' '], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
             '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'] }

	keypresses = ''
	last_digit = ''
	for char in msg:
		for digit, characters in d.items():
			if char in characters:
				if last_digit == digit:
					keypresses += ' '

				keypresses += digit * (characters.index(char)+1)
				last_digit = digit
				break

	print 'Case #%s: %s' % (caseno, ''.join(keypresses))
		

def main():
	cases = int(raw_input())
	for i in range(cases):
		msg = str(raw_input())
		translate(i+1, msg)


if __name__ == "__main__":
	main()
