####################################################################################################
#A Rescursive Implementation of the Longest Common Subsequence Problem
####################################################################################################
def lcs (a, b):
	if (not a or not b):
		return ('');
	if (a [-1] == b [-1]):
		return (lcs (a [ : -1], b [ : -1]) + a [-1]);

	first, second = lcs (a [ : -1], b), lcs (a, b [: -1]);
	return (first if len (first) > len (second) else second);

a, b = input (), input ();
#SAMPLE CALL TO THE FUNCTION
print (lcs (a, b));
