teamData = {}

with open('teamStats.txt') as input_file:
    for line in input_file:
        team, fg, fga, threeP, threePa, ft, fta, orb, drb, ast, stl, blk, tov, pf = line.split(' ')
        teamData[team] = dict(zip(('FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF'), (float(fg), float(fga), float(threeP), float(threePa), float(ft),
        float(fta), float(orb), float(drb), float(ast), float(stl), float(blk), float(blk),
        float(pf))))

def printInfo():
    print('initial info: ')
    for x in teamData:
        print(x)

def printTeam(x):
    print(x)
    print('FG: %.1f, FGA: %.1f' % (teamData[x]['FG'], teamData[x]['FGA']))
    print('3P: %.1f, 3PA: %.1f' % (teamData[x]['3P'], teamData[x]['3PA']))
    print('FT: %.1f, FTA: %.1f' % (teamData[x]['FT'], teamData[x]['FTA']))
    print('ORB: %.1f, DRB: %.1f, AST: %.1f' % (teamData[x]['ORB'], teamData[x]['DRB'], teamData[x]['AST']))
    print('STL: %.1f, BLK: %.1f' % (teamData[x]['STL'], teamData[x]['BLK']))
    print('TOV: %.1f, PF: %.1f' % (teamData[x]['TOV'], teamData[x]['PF']))

#printInfo()
