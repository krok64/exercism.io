def hey(phrase):
    phrase = phrase.strip()
    if phrase=="":
    	return 'Fine. Be that way!'
    if (phrase[-1]=="!" or phrase.isupper()) and not phrase.startswith('Let\'s'):
    	return 'Whoa, chill out!'
    if phrase[-1]=="?":
    	return 'Sure.'
    return 'Whatever.'