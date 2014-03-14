#!usr/env/python
#Modeling a soccer team with substitutions

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

        print "Added %s to the team!" % name


#Should list the players currently on the field. Only 3 player sample data
players_on_field = []
class OnField(object):
        def __init__(self):
            pass
        def sub_in(self, sub_name):
            self.sub_name = sub_name
            if len(players_on_field) == 3:
                print "Field is full, sub_out first!"
                #testing some options
                #x = raw_input('Which player would you like to sub out?')
                #OnField.sub_out(x)
            else:
                players_on_field.append(sub_name)
                print "%s entering the game" % sub_name
            return

        def sub_out(self, sub_name):
            for i in range(3):
                if players_on_field[i] == sub_name:
                    del players_on_field[i]
                    print "%s has been removed from the game" % sub_name
                    return
                #testing some options
                #x = raw_input('Who would you like to sub in?')
                #OnField.sub_in(x)
            else:
                print "That player is not on the field"
                return

        def list_players_on_field(self):
            print players_on_field



#Testing
Barcelona = Team('Barcelona')
this = Players()
game = OnField()

this.addPlayer('Messi', 10, 'forward')
this.addPlayer('Neymar', 11, 'forward')
this.addPlayer('Song', 9, 'midfield')
this.addPlayer('Valdes', 1, 'goalie')
this.addPlayer('Pique', 25, 'defense')
this.addPlayer('Pedro', 8, 'forward')

print players

print 'Forward Players'
print forward
print 'Midfield Players'
print midfield
print 'Defense Players'
print defense
print 'Goalies'
print goalie

#Subsitution testing
print "Players currently on the field"
print players_on_field
game.sub_in('Messi')
game.sub_in('Pedro')
game.sub_in('Song')
game.list_players_on_field()
game.sub_out('Pedro')
print players_on_field
game.sub_in('Neymar')
print players_on_field
