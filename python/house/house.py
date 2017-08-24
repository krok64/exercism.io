this_is = ["house that Jack built.", "malt", "rat", "cat", "dog", "cow with the crumpled horn", 
"maiden all forlorn", "man all tattered and torn", "priest all shaven and shorn", "rooster that crowed in the morn",
"farmer sowing his corn", "horse and the hound and the horn"]
that = ["lay in", "ate", "killed", "worried", "tossed", "milked", "kissed", "married", "woke", "kept", "belonged to"]


def verse(num):
    result = "This is the %s" % this_is[num]
    for i in range(num, 0, -1):
        result += "\nthat %s the %s" % (that[i-1], this_is[i-1])
    return result


def rhyme():
    result = ""
    for i in range(len(this_is)):
        result += verse(i) + "\n\n"
    return result[:-2]
