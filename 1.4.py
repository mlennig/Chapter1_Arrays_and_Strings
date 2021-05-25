s = "Tact Coa"
#s = 'abba'
#s = '123412345'
#s = ''
s = "dask dddd"
def isPalindromePossible(s):
	s = s.lower()
	s = s.replace(' ', '')
	nOdd = 0
	isEven = len(s) % 2 == 0			# Length of s is even
	
	charCounts = {}
	for character in s:
		charCounts[character] = 0
		
	for character in s:
		charCounts[character] += 1		
		
	print(charCounts)
	
	for character in charCounts.keys():
		if charCounts[character] % 2 != 0:
			nOdd += 1
			
	return nOdd <= 1


print(s, ' has permutations which can become palindromes: ', isPalindromePossible(s))




		
		

	
	
	
	
	
		
		