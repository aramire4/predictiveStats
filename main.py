from readFromFile import *

class main:
    def compareTeam(chosenTeam, otherTeam, data):
        w = 64.6 + (0.0743 * data[chosenTeam]['FG']) 
        - (0.0307 * data[chosenTeam]['FGA']) + (0.0194 * data[chosenTeam]['3P'])
        + (0.00513 * data[chosenTeam]['3PA']) + (0.0397 * data[chosenTeam]['FT']) 
        - (0.0155 * data[chosenTeam]['FTA']) + (0.0364 * data[chosenTeam]['ORB']) 
        + (0.00278 * data[chosenTeam]['DRB']) + (0.00332 * data[chosenTeam]['AST']) 
        + (0.0100 * data[chosenTeam]['STL']) + (0.00308 * data[chosenTeam]['BLK'])
        - (0.0169 * data[chosenTeam]['TOV']) - (0.00484 * data[chosenTeam]['PF'])
        
        opp = -(0.0605 * data[otherTeam]['FG']) + (0.0113 * data[otherTeam]['FGA']) 
        - (0.0378 * data[otherTeam]['3P']) + (0.00461 * data[otherTeam]['3PA'])
        - (0.0105 * data[otherTeam]['ORB']) + (0.0135 * data[otherTeam]['DRB'])
        + (0.00032 * data[otherTeam]['AST']) + (0.00181 * data[otherTeam]['STL']) 
        - (0.00751 * data[otherTeam]['BLK']) + (0.00544 * data[otherTeam]['TOV'])
        + (0.00214 * data[otherTeam]['PF'])

        return (w+opp)
    
    def compareAllTeams(chosenTeam, compareTeam, data):
        wins = 0.0
        games = 0.0
        for x in data:
            if x != chosenTeam:
                w = compareTeam(chosenTeam, x, data)
                opp = compareTeam(x, chosenTeam, data)
                if opp > w:
                    games += 1.0
                else:
                    wins += 1.0
                    games += 1.0
        print('Games won %.0f' % wins)
        print('Games played %.0f' % games)
        return float(wins/games)

    def comparePlayer(player, playerData, compareTeam, compareAllTeams):
        return(compareAllTeams(player, compareTeam, playerData))
        '''
        print('stats without the player:')
        printTeam(yourTeam, data)
        d = data
        if(playerData[player]['Team'] != data[yourTeam]):
            d[yourTeam]['FG'] = (data[yourTeam]['FG'] * 12 + playerData[player]['FG'])/12
            d[yourTeam]['FGA'] = (data[yourTeam]['FGA'] * 12 + playerData[player]['FGA'])/12
            d[yourTeam]['3P'] = (data[yourTeam]['3P'] * 12 + playerData[player]['3P'])/12
            d[yourTeam]['3PA'] = (data[yourTeam]['3PA'] * 12 + playerData[player]['3PA'])/12
            d[yourTeam]['FT'] = (data[yourTeam]['FT'] * 12 + playerData[player]['FT'])/12
            d[yourTeam]['FTA'] = (data[yourTeam]['FTA'] * 12 + playerData[player]['FTA'])/12
            d[yourTeam]['ORB'] = (data[yourTeam]['ORB'] * 12 + playerData[player]['ORB'])/12
            d[yourTeam]['DRB'] = (data[yourTeam]['DRB'] * 12 + playerData[player]['DRB'])/12
            d[yourTeam]['AST'] = (data[yourTeam]['AST'] * 12 + playerData[player]['AST'])/12
            d[yourTeam]['STL'] = (data[yourTeam]['STL'] * 12 + playerData[player]['STL'])/12
            d[yourTeam]['BLK'] = (data[yourTeam]['BLK'] * 12 + playerData[player]['BLK'])/12
            d[yourTeam]['TOV'] = (data[yourTeam]['TOV'] * 12 + playerData[player]['TOV'])/12
            d[yourTeam]['PF'] = (data[yourTeam]['PF'] * 12 + playerData[player]['PF'])/12
        else:
            d[yourTeam]['FG'] = (data[yourTeam]['FG'] * 12 - playerData[player]['FG'])/11
            d[yourTeam]['FGA'] = (data[yourTeam]['FGA'] * 12 - playerData[player]['FGA'])/11
            d[yourTeam]['3P'] = (data[yourTeam]['3P'] * 12 - playerData[player]['3P'])/11
            d[yourTeam]['3PA'] = (data[yourTeam]['3PA'] * 12 - playerData[player]['3PA'])/11
            d[yourTeam]['FT'] = (data[yourTeam]['FT'] * 12 - playerData[player]['FT'])/11
            d[yourTeam]['FTA'] = (data[yourTeam]['FTA'] * 12 - playerData[player]['FTA'])/11
            d[yourTeam]['ORB'] = (data[yourTeam]['ORB'] * 12 - playerData[player]['ORB'])/11
            d[yourTeam]['DRB'] = (data[yourTeam]['DRB'] * 12 - playerData[player]['DRB'])/11
            d[yourTeam]['AST'] = (data[yourTeam]['AST'] * 12 - playerData[player]['AST'])/11
            d[yourTeam]['STL'] = (data[yourTeam]['STL'] * 12 - playerData[player]['STL'])/11
            d[yourTeam]['BLK'] = (data[yourTeam]['BLK'] * 12 - playerData[player]['BLK'])/11
            d[yourTeam]['TOV'] = (data[yourTeam]['TOV'] * 12 - playerData[player]['TOV'])/11
            d[yourTeam]['PF'] = (data[yourTeam]['PF'] * 12 - playerData[player]['PF'])/11
        print('stats with the player:')
        printTeam(yourTeam, d)
        '''
        #per = compareAllTeams(yourTeam, compareTeam, d)
        #return per

    def getAverageStats(data):
        average = {}
        fg = 0
        fga = 0
        threeP = 0
        threePA = 0
        ft = 0
        fta = 0
        orb = 0
        drb = 0
        ast = 0
        stl = 0
        blk = 0
        tov = 0
        pf = 0
        teams = 0
        
        for x in data:
            teams += 1
            fg = (fg + data[x]['FG'])
            fga = (fga + data[x]['FGA'])
            threeP = (threeP + data[x]['3P'])
            threePA = (threePA + data[x]['3PA'])
            ft = (ft + data[x]['FT'])
            fta = (fta + data[x]['FTA'])
            orb = (orb + data[x]['ORB'])
            drb = (drb + data[x]['DRB'])
            ast = (ast + data[x]['AST'])
            stl = (stl + data[x]['STL'])
            blk = (blk + data[x]['BLK'])
            tov = (tov + data[x]['TOV'])
            pf = (pf + data[x]['PF'])

        fg /= teams
        fga /= teams
        threeP /= teams
        threePA /= teams
        ft /= teams
        fta /= teams
        orb /= teams
        drb /= teams
        ast /= teams
        stl /= teams
        blk /= teams
        tov /= teams
        pf /= teams

        average['average'] = dict(zip(('FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF'), (float(fg), float(fga), float(threeP), float(threePA), float(ft),
        float(fta), float(orb), float(drb), float(ast), float(stl), float(blk), float(tov), float(pf))))

        return average
    
    def runWithAverages(team, avg, data, avgData):
        stats = {}
        fg = data[team]['FG'] - avgData[avg]['FG']
        fga = data[team]['FGA'] - avgData[avg]['FGA']
        threeP = data[team]['3P'] - avgData[avg]['3P']
        threePA = teamData[team]['3PA'] - avgData[avg]['3PA']
        ft = data[team]['FT'] - avgData[avg]['FT']
        fta = data[team]['FTA'] - avgData[avg]['FTA']
        orb = data[team]['ORB'] - avgData[avg]['ORB']
        drb = data[team]['DRB'] - avgData[avg]['DRB']
        ast = data[team]['AST'] - avgData[avg]['AST']
        stl = data[team]['STL'] - avgData[avg]['STL']
        blk = data[team]['BLK'] - avgData[avg]['BLK']
        tov = data[team]['TOV'] - avgData[avg]['TOV']
        pf = data[team]['PF'] - avgData[avg]['PF']
        
        stats['stats'] = dict(zip(('FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST',
        'STL', 'BLK', 'TOV', 'PF'), (float(fg), float(fga), float(threeP), float(threePA), float(ft),
        float(fta), float(orb), float(drb), float(ast), float(stl), float(blk), float(tov), float(pf))))

        return stats
        
    def calculateWeights(s, sts, weights):
        improvements = {}

        fg = sts[s]['FG'] * weights['FG']
        fga = sts[s]['FGA'] * weights['FGA']
        threeP = sts[s]['3P'] * weights['3P']
        threePA = sts[s]['3PA'] * weights['3PA']
        ft = sts[s]['FT'] * weights['FT']
        fta = sts[s]['FTA'] * weights['FTA']
        orb = sts[s]['ORB'] * weights['ORB']
        drb = sts[s]['DRB'] * weights['DRB']
        ast = sts[s]['AST'] * weights['AST']
        stl = sts[s]['STL'] * weights['STL']
        blk = sts[s]['BLK'] * weights['BLK']
        tov = sts[s]['TOV'] * weights['TOV']
        pf = sts[s]['PF'] * weights['PF']

        improvements = dict([('FG', fg), ('FT', ft), ('ORB', orb), ('FGA', fga), ('3P',
        threeP), ('TOV', tov), ('FTA', fta), ('STL', stl), ('3PA', threePA), ('PF', pf),
        ('AST', ast), ('BLK', blk), ('DRB', drb)])

        return improvements
        

    print('a) see team stats')
    print('b) compare  2 teams')
    print('c) compare a team with the league')
    print('d) should I hire this player')
    print('e) what does my team need?')
    choice = raw_input('what do you want to do? ')
    choice = choice.rstrip('\n')

    info = {}
    teamOrder = []

    if choice is 'a' or choice is 'A':
        printInfo(teamData)
        t = raw_input('\npick a team ').rstrip('\n')
        printTeam(t, teamData)
    
    elif choice is 'b' or choice is 'B':
        printInfo(teamData)
        t = raw_input('\npick a team ').rstrip('\n')
        o = raw_input('pick another team ').rstrip('\n')
        w = compareTeam(t, o, teamData)
        print('Wins for %s: %f' % (t, w))
        w2 = compareTeam(o, t, teamData)
        print('Wins for %s: %f' % (o, w2))
        print('difference %f' % (abs(w-w2)))

    elif choice is 'c' or choice is 'C':
        printInfo(teamData)
        t = raw_input('\npick a team ').rstrip('\n')
        per = compareAllTeams(t, compareTeam, teamData) 
        print(per)

    elif choice is 'd' or choice is 'D':
        #td = teamData
        for x in freeAgents:
            print(x)
        p = raw_input('\npick a player ').rstrip('\n')
        per = comparePlayer(p, freeAgents, compareTeam, compareAllTeams)
        print(per)
        '''
        print('with this player %s' % per)
        #per = compareTeam(t, t, teamData)
        per = compareAllTeams(t, compareTeam, teamData) 
        print('without this player %s' % per)
        '''
        #print('To be done')

    else:
        weights = dict([('FG', 0.074), ('FT', 0.040), ('ORB', 0.036), ('FGA', -0.031), ('3P',
        0.019), ('TOV', -0.017), ('FTA', -0.016), ('STL', 0.010), ('3PA', 0.005), ('PF', -0.005),
        ('AST', 0.003), ('BLK', 0.003), ('DRB', 0.003)])
        #Attempts should be lower, appart from 3PA
        printInfo(teamData)
        t = raw_input('\npick a team ').rstrip('\n')
        avg = getAverageStats(teamData)
        printTeam('average', avg)
        printTeam(t, teamData)
        sts = runWithAverages(t, 'average', teamData, avg)
        printTeam('stats', sts)
        improvements = calculateWeights('stats', sts, weights)
        lst = sorted(improvements, key=improvements.get, reverse=False)
        print(lst)
        lst = lst[:5]



