teamData = {}
freeAgents = {}

with open('teamStats.txt') as input_file:
    for line in input_file:
        team, fg, fga, threeP, threePa, ft, fta, orb, drb, ast, stl, blk, tov, pf = line.split(' ')
        teamData[team] = dict(zip(('FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF'), (float(fg), float(fga), float(threeP), float(threePa), float(ft),
        float(fta), float(orb), float(drb), float(ast), float(stl), float(blk), float(blk),
        float(pf))))


with open('freeAgents.txt') as input_file:
    for line in input_file:
        player, fg, fga, threeP, threePa, ft, fta, orb, drb, ast, stl, blk, tov, pf, team= line.split(' ')
        freeAgents[player] = dict(zip(('FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF', 'Team'), (float(fg), float(fga), float(threeP), float(threePa), float(ft),
        float(fta), float(orb), float(drb), float(ast), float(stl), float(blk), float(blk),
        float(pf), team)))


def printInfo(data):
    print('initial info: ')
    for x in data:
        print(x)

def printTeam(x, data):
    print(x)
    print('FG: %.1f, FGA: %.1f' % (data[x]['FG'], data[x]['FGA']))
    print('3P: %.1f, 3PA: %.1f' % (data[x]['3P'], data[x]['3PA']))
    print('FT: %.1f, FTA: %.1f' % (data[x]['FT'], data[x]['FTA']))
    print('ORB: %.1f, DRB: %.1f, AST: %.1f' % (data[x]['ORB'], data[x]['DRB'], data[x]['AST']))
    print('STL: %.1f, BLK: %.1f' % (data[x]['STL'], data[x]['BLK']))
    print('TOV: %.1f, PF: %.1f' % (data[x]['TOV'], data[x]['PF']))
    print('')

#printInfo()
