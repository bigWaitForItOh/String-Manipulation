##########################################################################################################
#Get All Possible Permutations of a given String
#Time Complexity: O (N!)
#Space Complexity: O (N!)
##########################################################################################################

results = [];

def get_perm (string, chr_status, current_perm, start):
	if (start == len (string)):
		results.append (current_perm);
		return;

	for i in range (len (string)):
		if (chr_status [i] == False):
			continue;
		current_perm [start] = string [i];
		chr_status [i] = False;
		get_perm (string, chr_status, current_perm, start+1);
		chr_status [i] = True;

def permutations (string):
	chr_status = [True for char in string];
	get_perm (string, chr_status, [None for i in range (len (string))], 0);

if (__name__ == '__main__'):
	permutations (input ());
	for i in results: print (i);