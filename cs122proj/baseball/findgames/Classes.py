#player class


class Players:

    def __init__(self, namefirst, namelast, position, player_id):
        self.firstname = namefirst
        self.lastname = namelast
        self.position = position
        self.player_id = player_id
        self.years_played = None
        self.stats = {}
        self.ranks = {}
        self.power_index = 0
        self.war = 0


    def add_stats(self, stat, value):
        '''
        stats should be a list of tuples in the form
        '''
        self.stats[stat] = value

    def add_war(self, war):
        self.war += war

    def add_years(self, years):
        self.years_played = years

    def add_rank(self, category, ranking):
        self.ranks[category] = ranking

    def incr_power_index(self, num):
        self.power_index += num

    def __repr__(self):
        str_var = '{} {} -- {}: {}'.format(self.firstname, self.lastname, self.position, self.power_index)
        return str_var

class Teams:

    def __init__(self):
        self.roster = {'Catcher': [], 'First Baseman': [], 'Second Baseman': 
        [], 'Designated Hitter': [], 'Third Baseman': [], 'Shortstop': [], 'Leftfielder': [], 'Centerfielder': [], 'Rightfielder': [], 'Pitcher': []}
        self.pos_filled = 0
        self.team_size = 0
        self.max_size = 25
        self.pitchers_needed = 8
        self.team_war = 0
        self.team_stats = {}
        self.total_pos = 10

    def add_player(self, player):
        '''
        player is a Player object
        '''
        if player.position != 'Pitcher':
            if len(self.roster[player.position]) == 0:
                self.roster[player.position] += [player]
                self.team_size += 1
                self.pos_filled += 1
            elif len(self.roster[player.position]) < 2:
                self.roster[player.position] += [player]
                self.team_size += 1
            else:
                self.look_for_player_to_replace(player)
        else:
            if len(self.roster['Pitcher']) == 0:
                self.roster['Pitcher'] += [player]
                self.team_size += 1
                self.pos_filled += 1
            elif len(self.roster['Pitcher']) < self.pitchers_needed:
                self.roster['Pitcher'] += [player]
                self.team_size += 1
            else:
                self.look_for_player_to_replace(player)
            

    def is_safe_to_add(self, player):
        return (self.total_pos - self.pos_filled != self.max_size - self.team_size) and (len(self.roster[player.position]) < 2)

    def look_for_player_to_replace(self, player):
        for dude in self.roster[player.position]:
            if player.power_index > dude.power_index:
                self.roster[player.position].remove(dude)
                self.roster[player.position].append(player)
                break

    def add_stat(self, statname, value):
        self.team_stats[statname] = value

    def __repr__(self):
        str_var = ''
        for i in self.roster:
            str_var += i + ': '
            for j in self.roster[i]:
                str_var += j.firstname + ' ' + j.lastname + ' \n'
        return str_var
