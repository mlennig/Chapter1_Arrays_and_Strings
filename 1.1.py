#s = 'adebathead'
s1 = 'deajbkilt'
s2 = '9876544'
#s = ''.join(sorted(s))
#print(s)

#s_dict = {}
#for i in range(len(s)):
	#s_dict[s[i]] = s[i] 
#print(s_dict)

#for i in range(len(s) - 1):
	#if s[i] == s[i + 1]:
		#print('The chars in this string are not unique.')
		#break

#print('The loop is finished.')

def isUniqueChars(s):
	if len(s) > 128: 
		return False
	char_set = [False for i in range(128)]
	for i in range(len(s)):
		if char_set[ord(s[i])]:
			return False
		else:
			char_set[ord(s[i])] = True
	return True
	
	
print('s1 has all unique characters: ', isUniqueChars(s1))
print('s2 has all unique characters: ', isUniqueChars(s2))

# Using a bit vector 
# Assume all characters are lowercase letters a-z
def isUniqueChars(s):
	checker = 0
	if len(s) > 27: 
		return False

	for i in range(len(s)):
		val = ord(s[i]) - 'a'
	return True