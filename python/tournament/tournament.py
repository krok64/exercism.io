def tally(data):
    result = ['Team                           | MP |  W |  D |  L |  P']
    teams = []
    if data != '':
        for match in data.split("\n"):
            team1, team2, rez = match.split(";")
            if rez=="win":
                win(teams, team1)
                lose(teams, team2)
            elif rez=="loss":
                lose(teams, team1)
                win(teams, team2)
            elif rez=="draw":
                draw(teams, team1)
                draw(teams, team2)
            else:
                raise ValueError(rez)
        teams.sort(key=lambda datum: (-datum['P'], datum['name']))
        for i in range(len(teams)):
            result.append("%-31s|%3d |%3d |%3d |%3d |%3d" % (teams[i]['name'], teams[i]['MP'], teams[i]['W'], teams[i]['D'], teams[i]['L'], teams[i]['P']))

    return "\n".join(result)


def get_name_index(teams, t_name):
    for x in range(len(teams)):
        if teams[x]['name'] == t_name:
            return x
    return -1


def win(teams, name):
    idx = get_name_index(teams, name)
    if idx != -1:
        teams[idx]['MP'] += 1
        teams[idx]['W'] += 1
        teams[idx]['P'] += 3
    else:
        teams.append({'MP':1, 'W':1, 'D':0, 'L':0, 'P':3, 'name':name})


def lose(teams, name):
    idx = get_name_index(teams, name)
    if idx != -1:
        teams[idx]['MP'] += 1
        teams[idx]['L'] += 1
    else:
        teams.append({'MP':1, 'W':0, 'D':0, 'L':1, 'P':0, 'name':name})


def draw(teams, name):
    idx = get_name_index(teams, name)
    if idx != -1:
        teams[idx]['MP'] += 1
        teams[idx]['D'] += 1
        teams[idx]['P'] += 1
    else:
        teams.append({'MP':1, 'W':0, 'D':1, 'L':0, 'P':1, 'name':name})

if __name__ == '__main__':
    results = ('Courageous Californians;Devastating Donkeys;win\n'
                   'Allegoric Alaskans;Blithering Badgers;win\n'
                   'Devastating Donkeys;Allegoric Alaskans;loss\n'
                   'Courageous Californians;Blithering Badgers;win\n'
                   'Blithering Badgers;Devastating Donkeys;draw\n'
                   'Allegoric Alaskans;Courageous Californians;draw')
    print(tally(results))