#!usr/env/python
#Modeling a soccer team roster

#Players stored in dictionary {Name:Numbers}
players = {}
# Player positions stored in a list
forward = []
midfield = []
defense = []
goalie = []

class Team(object):
    def __init__(self, name):
        self.name = name


class Players(object):
    def __init__(self):
        pass
#creates a player list with names, numbers, and preferred positions
    def addPlayer(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position
        players[name] = number
        print "Added %s to the team!" % name

#there has to be a better way to add positions. Recursive call to addPlayer????
    def Positions(self, name, position):
        self.name = name
        self.position = position

        if position == 'forward':
            forward.append(name)
            return forward
        elif position == 'midfield':
            midfield.append(name)
            return midfield
        elif position == 'defense':
            defense.append(name)
            return defense
        elif position == 'goalie':
            goalie.append(name)
            return goalie
        else:
            print 'Only forward, midfield, defense, goalie accepted'




Barcelona = Team('Barcelona')
this = Players()



this.addPlayer('Messi', 10, 'forward')
this.addPlayer('Neymar', 11, 'forward')
this.addPlayer('Song', 9, 'midfield')
this.addPlayer('Valdes', 1, 'goalie')
this.addPlayer('Pique', 25, 'defense')

print players

this.Positions('Messi', 'forward')
this.Positions('Valdes', 'goalie')
print 'Forward Players'
print forward
print 'Midfield Players'
print midfield
print 'Defense Players'
print defense
print 'Goalies'
print goalie



