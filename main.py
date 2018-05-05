from readFromFile import *

class main:
    def compareTeam(chosenTeam, otherTeam):
        w = 64.6 + (0.0743 * teamData[chosenTeam]['FG']) 
        - (0.0307 * teamData[chosenTeam]['FGA']) + (0.0194 * teamData[chosenTeam]['3P'])
        + (0.00513 * teamData[chosenTeam]['3PA']) + (0.0397 * teamData[chosenTeam]['FT']) 
        - (0.0155 * teamData[chosenTeam]['FTA']) + (0.0364 * teamData[chosenTeam]['ORB']) 
        + (0.00278 * teamData[chosenTeam]['DRB']) + (0.00332 * teamData[chosenTeam]['AST']) 
        + (0.0100 * teamData[chosenTeam]['STL']) + (0.00308 * teamData[chosenTeam]['BLK'])
        - (0.0169 * teamData[chosenTeam]['TOV']) - (0.00484 * teamData[chosenTeam]['PF'])
        
        opp = -(0.0605 * teamData[otherTeam]['FG']) + (0.0113 * teamData[otherTeam]['FGA']) 
        - (0.0378 * teamData[otherTeam]['3P']) + (0.00461 * teamData[otherTeam]['3PA'])
        - (0.0105 * teamData[otherTeam]['ORB']) + (0.0135 * teamData[otherTeam]['DRB'])
        + (0.00032 * teamData[otherTeam]['AST']) + (0.00181 * teamData[otherTeam]['STL']) 
        - (0.00751 * teamData[otherTeam]['BLK']) + (0.00544 * teamData[otherTeam]['TOV'])
        + (0.00214 * teamData[otherTeam]['PF'])

        return (w+opp)
    
    def compareAllTeams(chosenTeam, compareTeam):
        wins = 0.0
        games = 0.0
        for x in teamData:
            if x != chosenTeam:
                w = compareTeam(chosenTeam, x)
                opp = compareTeam(x, chosenTeam)
                if opp > w:
                    games += 1.0
                else:
                    wins += 1.0
                    games += 1.0
        print('Games won %.0f' % wins)
        print('Games played %.0f' % games)
        return float(wins/games)

    print('a) see team stats')
    print('b) compare  2 teams')
    print('c) compare a team with the league')
    print('d) find what a team needs')
    choice = raw_input('what do you want to do? ')
    choice = choice.rstrip('\n')

    info = {}
    teamOrder = []
    for x in teamData:
        print(x)
    t = raw_input('\npick a team ').rstrip('\n')

    if choice is 'a' or choice is 'A':
        printTeam(t)
    
    elif choice is 'b' or choice is 'B':
        o = raw_input('pick another team ').rstrip('\n')
        w = compareTeam(t, o)
        print('Wins for %s: %f' % (t, w))
        w2 = compareTeam(o, t)
        print('Wins for %s: %f' % (o, w2))
        print('difference %f' % (abs(w-w2)))

    elif choice is 'c' or choice is 'C':
       per = compareAllTeams(t, compareTeam) 
       print(per)

    else:
        print('To be done')
