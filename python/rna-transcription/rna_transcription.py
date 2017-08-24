def to_rna(word):

	result=""
	for ch in word:
		if ch=='G':
			result=result+'C'
		elif ch=='C':
			result=result+'G'
		elif ch=='T':
			result=result+'A'
		elif ch=='A':
			result=result+'U'
		else:
			return ''

	return result
