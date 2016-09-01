"""
A phone answering machine receives a word dialed on the numeric pad as a string of digits. One keypress per letter, like in the old Nokia T9. For example, 228 for "CAT". But it could also mean "BAT". Write a function that receives the digits and a dictionary and returns all the possible matching words.
"""
import sys

class Tree(object):
  def __init__(self, data):
    self.data = data
    self.children = []

  def insert_child(self, data):
    self.children.append(Tree(data))

  def __repr__(self):
    return 'Data: %s, Children: %s' % (self.data, self.children)


def print_tree(node, word):
  """ preorder traversal """
  
  word += node.data
  if not len(node.children):
     print word
     return
  else:
    for node in node.children:
      print_tree(node, word)


def match_words(digits, dictionary):
  result = []
  root_trees = []

  for char in dictionary[digits[0]]:
    root_trees.append(Tree(char))
    adjacent_nodes = [root_trees[-1]]
    for digit in digits[1:]:
      adj_nodes = []
      for node in adjacent_nodes:
        for char in dictionary[digit]:
          node.insert_child(char)
        adj_nodes.extend(node.children)
      adjacent_nodes = adj_nodes

  for tree in root_trees:
    print_tree(tree, "")

def main():
  if len(sys.argv) != 2:
    sys.stdout.write("Usage: " + sys.argv[0] + " digits")
    sys.exit(1)
 
  dictionary = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': [' ']}
 
  match_words(sys.argv[1], dictionary)
		

if __name__ == "__main__":
	main()

"""
228
a b c
a b c
t u v

1.aat
2.aau
3.aav
4.abt
5.abu
6.abv
7.act
8.acu
9.acv
10.bat
11.bau
12.bav
13.bbt
14.bbu
15.bbv
16.bct
17.bcu
18.bcv
19.cat
20.cau
21.cav
22.cbt
23.cbu
24.cbv
25.cct
26.ccu
27.ccv

tree:
        a			b
  a     b     c		  a     b     c
t u v t u v t u v       t u v t u v t u v

"""
