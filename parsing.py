from string import *
import ast

def remove_h(formula):
	"""Takes standard structural chemical formula, and removes all hydrogens from the formula.

	formula: string
	Returns: string
	"""
	#Just in case someone decides to enter non-capital letters...I've made that mistake before :P
	s = formula.upper()

	#Replaces all possible combinations of hydrogens with the empty string.Important: this function call replaces 'H' last!
	res = s.replace('H4','').replace('H3','').replace('H2','').replace('H','')

	return res

def make_list(formula):
	"""Takes a stripped formula (i.e. a structural formula which has gone through remove_h()) and converts it to a nested list.

	TODO: handle formulas with parenthetical multiplicity, ex. C(CH3)3

	TODO: make this function less gross-string-manipulation-ish.

	formula: string
	Returns: list
	"""
	t = list(formula)

	#Puts spaces between each character, then concatenates list into a string.The spaces are important here because I'm using the split() method to split the string into elements of a list in the eval() function call.
	t2 = ''.join([c + ' ' for c in t])

	#Splits the string into elements by spaces, replaces parentheses with brackets, then evaluates the resulting expression as a Python expression. The result is a list. 
	return eval(str(t2.split()).replace("'(',", '[').replace("')'",']'))



def main():
	#the basics
	s1 = 'CH3CH2CH3'
	print 's1:',
	print remove_h(s1)

	#test case for mixed upper/lowercase letters
	s2 = 'Ch3Ch2cH3'
	print 's2:',
	print remove_h(s2)

	#different types of central atoms
	s3 = 'CH3CH2NH2'
	print 's3:',
	print remove_h(s3)

	#ooh! nesting!
	s4 = 'CH3CH2CH(CH3)CH2CH3'
	print 's4:',
	print remove_h(s4)
	print make_list(remove_h(s4))

	#hard mode
	s5 = 'CH3CH2CH(CH3CH(CH3)CH3)CH2CH3'
	print 's5:',
	print remove_h(s5)
	print make_list(remove_h(s5))

	#EXTREEEEEME!
	s6 = 'HOCH2(CH3CH2CH(CH2CH3)CH2CH3)CH(CH3)CH2NH2'
	print 's6:',
	print remove_h(s6)
	print make_list(remove_h(s6))

if __name__ == '__main__':
	main()