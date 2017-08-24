import itertools


def solution():
    house_colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
    nations = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
    pets = ["dog", "snails", "fox", "horse", "zebra"]
    drinks = ["coffee", "tea", "milk", "orange juice", "water"]
    smokes = ["Old Good", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"]

    for house in itertools.permutations(house_colors):
        for i in range(4):
            if house[i] == "Ivory" and house[i+1] == "Green" and house[1] == "Blue":
                for man in itertools.permutations(nations):
                    for j in range(5):
                        if man[j] == "Englishman" and house[j] == "Red" and man[0] == "Norwegian":
                            for drink in itertools.permutations(drinks):
                                for k in (0, 1, 3, 4):
                                    if man[k] == "Ukrainian" and drink[k] == "tea" and drink[2] == "milk":
                                        for l in (0, 1, 3, 4):
                                            if drink[l] == "coffee" and house[l] == "Green":
                                                for smoke in itertools.permutations(smokes):
                                                    for a in range(5):
                                                        if man[a]=="Japanese" and smoke[a]=="Parliaments":
                                                            for b in range(5):
                                                                if house[b]=="Yellow" and smoke[b]=="Kools":
                                                                    for c in range(5):
                                                                        if drink[c]=="orange juice" and smoke[c]=="Lucky Strike":
                                                                            for pet in itertools.permutations(pets):
                                                                                for d in range(5):
                                                                                    if man[d]== "Spaniard" and pet[d]=="dog":
                                                                                        for f in range(5):
                                                                                            if smoke[f]=="Old Good"  and pet[f]=="snails":
                                                                                                for g in range(5):
                                                                                                    if smoke[g]=="Chesterfields" and (g>0 and pet[g-1]=="fox" or g<4 and pet[g+1]=="fox"):
                                                                                                        for h in range(5):
                                                                                                            if smoke[h]== "Kools" and (h>0 and pet[h-1]=="horse" or h<4 and pet[h+1]=="horse"):
                                                                                                                for water_idx in range(5):
                                                                                                                    if drink[water_idx] == "water":
                                                                                                                        break
                                                                                                                for zebra_idx in range(5):
                                                                                                                    if pet[zebra_idx] == "zebra":
                                                                                                                        break
                                                                                                                return "It is the %s who drinks the water.\nThe %s keeps the zebra." % (man[water_idx], man[zebra_idx])

