#########################################################################################################
#Generate all possible Combinations of a string
#Time Complexity: O (2^N)
#Space Complexity: O (2^N)
#########################################################################################################

result = [];

def combinations (string):
	global result;
	for i in range (len (string)-1, -1, -1):
		temp = [string [i]];
		for word in result:
			temp.append (temp [0] + word);
		result += temp;

if (__name__ == '__main__'):
	combinations (input ());
	for i in result:
		print (i);