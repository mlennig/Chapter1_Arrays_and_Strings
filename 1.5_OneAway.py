

def OneAway(s1, s2):
	chars_s1 = [0 for i in range(128)]
	chars_s2 = [0 for i in range(128)]
	if len(s1) != len(s2):
		print('True')
		return True
	s1.lower()
	s2.lower()
	for i in range(len(s1)):
		chars_s1[ord(s1[i])] = i+1
	print(chars_s1)
	for i in range(len(s2)):
		chars_s2[ord(s2[i])] = i+1
	print(chars_s2)
	
	print(str(chars_s1 != chars_s2))

	return chars_s1 != chars_s2

string1 = "pale"
string2 = "ple"

str1 = "pale"
str2 = "bale"

OneAway(str1,str2)