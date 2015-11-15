####################################################################################################
#A Rescursive Implementation of the Longest Common Subsequence Problem
####################################################################################################
def lcs (x, y):
	if (not (x and y):
		return (0);
	if (x [-1] == y [-1]):
		return (1 + lcs (x [ : -1], y [ : -1]));
	return (max (lcs (x [ : -1], y), lcs (x, y [ : -1])));

a, b = input (), input ();
#SAMPLE CALL TO THE FUNCTION
print (lcs (a, b));
