class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.points = 0
        self.assists = 0
        self.rebounds = 0
    
    def update_stats(self, points, assists, rebounds):
        self.points += points
        self.assists += assists
        self.rebounds += rebounds
    
    def get_stats(self):
        return f"{self.name}: {self.points} PTS, {self.assists} AST, {self.rebounds} REB"


class Team:
    MAX_PLAYERS = 12
    
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []
        self.wins = 0
        self.losses = 0
    
    def add_player(self, player):
        if len(self.players) < Team.MAX_PLAYERS:
            self.players.append(player)
            return f"{player.name} has been added to {self.name}."
        return f"Cannot add {player.name}, {self.name} is full."
    
    def record_win(self):
        self.wins += 1
    
    def record_loss(self):
        self.losses += 1
    
    def get_record(self):
        return f"{self.name}: {self.wins} Wins, {self.losses} Losses"
    

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 0
        self.team2_score = 0
        self.is_played = False
    
    def record_result(self, team1_score, team2_score, player_stats):
        if self.is_played:
            return "Game result already recorded."
        
        self.team1_score = team1_score
        self.team2_score = team2_score
        
        if team1_score > team2_score:
            self.team1.record_win()
            self.team2.record_loss()
        else:
            self.team2.record_win()
            self.team1.record_loss()
        
        for player, stats in player_stats.items():
            player.update_stats(*stats)  # Unpacks (points, assists, rebounds)
        
        self.is_played = True
        return f"Game recorded: {self.team1.name} {team1_score} - {team2_score} {self.team2.name}"
    

class League:
    def __init__(self):
        self.teams = []
        self.games = []
    
    def add_team(self, team):
        self.teams.append(team)
        return f"{team.name} has joined the league."
    
    def schedule_game(self, team1, team2):
        if team1 not in self.teams or team2 not in self.teams:
            return "Both teams must be in the league to schedule a game."
        game = Game(team1, team2)
        self.games.append(game)
        return f"Game scheduled: {team1.name} vs {team2.name}"
    
    def get_standings(self):
        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)
        return [team.get_record() for team in sorted_teams]
