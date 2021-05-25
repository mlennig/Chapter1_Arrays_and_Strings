s1 = 'bbaaby'
s2 = 'ybbbaa'

def arePermutations(s1, s2):
	if len(s1) != len(s2): 
		return False
	char_set1 = [0 for i in range(128)]
	char_set2 = [0 for i in range(128)]
	for i in range(len(s1)):
		char_set1[ord(s1[i])] += 1
	for i in range(len(s2)):
		char_set2[ord(s2[i])] += 1	
	return char_set1 == char_set2

print(s1, ' and ', s2, ' are permutations of one another: ', arePermutations(s1,s2))