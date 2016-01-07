##############################################################################################################################
#Implementation of Knuth-Morris-Pratt Substring Search Algorithm
#Returns the index of the first substring matched in the main string.
#Complexities:
#	Time:
#		O (n) - construction of tracker, n is the length of substring
#		O (m) - running KMP with the help of tracker array, m is the length of main string
#		O (m + n) - total time complexity of the algorithm
#	Space:
#		O (n) - to store tracker array, n is the length of substring
##############################################################################################################################

def construct_tracker (substring):
	tracker = [None for i in range (len (substring))];
	j, i = 0, 1;

	tracker [0] = 0;
	while (i < len (tracker)):
		while ( (not substring [i] == substring [j]) and j > 0):
			j = tracker [j - 1];

		if (substring [i] == substring [j]):
			tracker [i] = j + 1;
			j += 1;
		else:
			tracker [i] = 0;

		i += 1;

	return (tracker);

def kmp (string, substring):
	tracker = construct_tracker (substring);
	positions, j = [], 0;

	for i in range (len (string)):
		if (string [i] == substring [j]):
			if (j == len (substring) - 1):
				positions.append (i - len (substring) + 1);
			else:
				j += 1;
		else:
			j = tracker [j - 1];

	return (positions);

if (__name__ == '__main__'):
	#string, substring = input (), input ();
	#print (kmp (string, substring));

	print (kmp ('abcxabcdabxabcdabcdabcyiuhsiuhduiahdubhbuuabcdabcysbhbh', 'abcdabcy'));
