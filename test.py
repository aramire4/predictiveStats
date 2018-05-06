
x = 1
hold = []
with open('freeAgents.txt') as input_file:
    for line in input_file:
        hold = line.split(' ')
        if len(hold) != 14:
            print('line %s items: %s' % (x, len(hold)))
        hold = []
        x+=1
        
        
