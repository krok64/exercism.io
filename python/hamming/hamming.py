def distance(dna1, dna2):
    if len(dna1) != len(dna2):
    	raise ValueError
    dist=0
    for idx, ch in enumerate(dna1):
    	if ch!=dna2[idx]:
    		dist=dist+1

    return dist
