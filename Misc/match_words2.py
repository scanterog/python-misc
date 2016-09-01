"""
A phone answering machine receives a word dialed on the numeric pad as a string of digits. One keypress per letter, like in the old Nokia T9. For example, 228 for "CAT". But it could also mean "BAT". Write a function that receives the digits and a dictionary and returns all the possible matching words.
"""

import sys

def gen_words(digits, dictionary):
   d = digits[0]
   for letter in dictionary[d]:
     if len(digits) == 1:
       yield letter
     else:
       for word in gen_words(digits[1:], dictionary):
          yield letter + word


def main():
  if len(sys.argv) != 2:
    sys.stdout.write("Usage: " + sys.argv[0] + " digits")
    sys.exit(1)
 
  dictionary = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': [' ']}
 
  for word in gen_words(sys.argv[1], dictionary):
    print word    

if __name__ == "__main__":
  main()

