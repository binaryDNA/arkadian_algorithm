import itertools

line = "-"* 85
print line 
print "Demonstration of an Arkadian Algorithm in Python"
print line 
print "Arkadian algorithms are algorithms that can reduce a sequence of 64 binary numbers,"
print "to 21 unique outputs, matching exactly the output of the protein synthesis process."


# Generating the 64 binary inputs, from 0 to 63.
BinaryInput64  =["".join(a) for a in itertools.product(["0", "1"], repeat=6)]
#print BinaryInput64

# ###########################################
# NAND GATE - SIMPLE DEFINITION
#
# the truth table is:
# INPUT X   INPUT Y   OUTPUT
#	0	0	1
#	0	1	1
#	1	0	1
#	1	1	0
# in other words:
# If the product of the inputs is 0, then the output is 1.
# If the product of the inputs is 1, then the output is 0.

def n(x,y):
	if x*y==0:return 1
	else: return 0
# ###########################################

# ###########################################
# QUATERNARY CONVERSION
#
# If we pass this function a 6-digit binary number, 
# it returns the 3 letter quaternary equivalent.

def q(x):
	def letter(L):
		if L=="00": return "A"
		if L=="01": return "C"
		if L=="10": return "G"
		if L=="11": return "U"
	a = letter(x[0:2])
	b = letter(x[2:4])
	c = letter(x[4:])
	
	return a+b+c
# ###########################################

# ###########################################
# Arkadian Algorithm - Python code for the dendrograms shown in the 
# book, BINARY NATURE, published in October 2013.

def arkadian(input):
	a = int(input[0])
	b = int(input[1])
	c = int(input[2])
	d = int(input[3])
	e = int(input[4])
	f = int(input[5])
	
	A =  n(n(n(n(n(n(n(f,f),c),b),c),f),n(n(n(n(n(b,d),c),c),a),n(n(c,d),f))),n(a,f))
	B =  n(n(n(n(n(a,c),n(c,d)),c),c),n(b,b))
	C =  n(n(n(n(n(a,f),a),n(n(n(b,f),d),c)),n(n(n(a,d),b),n(n(n(a,a),n(n(c,f),c)),c))),n(c,d))
	D =  n(n(n(n(n(n(n(b,f),f),c),n(a,f)),c),c),n(d,d))
	E =  n(n(n(n(n(n(n(n(c,c),e),n(n(a,f),b)),n(n(a,b),c)),n(n(n(n(d,e),d),n(d,f)),n(n(b,e),a))),n(b,e)),c),n(b,d))
	F =  n(n(n(n(a,b),d),n(n(n(a,b),c),n(n(n(n(b,b),b),d),f))),n(b,d))
	
	return str(A)+str(B)+str(C)+str(D)+str(E)+str(F)
# ###########################################

# ###########################################	


# in binary view
aminoacids = {}
for input in BinaryInput64:
	output = arkadian(input) 
	if output in aminoacids: aminoacids[output] = aminoacids[output] + ", " + input
	if output not in aminoacids: aminoacids[output] = input
print line 
print "Binary View:\n"
for t in aminoacids: print (t), " is the output of ", aminoacids[t]	

print ""

# in quaternary view
aminoacids = {}
for input in BinaryInput64:
	output = arkadian(input) 
	if q(output) in aminoacids: aminoacids[q(output)] = aminoacids[q(output)] + ", " + q(input)
	if q(output) not in aminoacids: aminoacids[q(output)] = q(input)
print line 
print "Quaternary View:\n"
for t in aminoacids: print (t), " is the output of ", aminoacids[t]	
	
print line 
print "\nCompare the Quaternary output of this program to the RNA Codon Table:"
print "http://en.wikipedia.org/wiki/RNA_codon_table#RNA_codon_table\n"
print "For more information on the concept of the Arkadian algorithms and the"
print "binary nature of our genetic code, please visit http://dna.mitsinikos.net"
print line 
