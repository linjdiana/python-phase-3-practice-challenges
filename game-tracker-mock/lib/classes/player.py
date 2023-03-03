from classes.result import Result

class Player:
    def __init__(self, username):
        self.username = username
    
    def get_username(self):
        return self._username
    def set_username(self, username):
        if isinstance(username, str) and (2 <= len(username) <= 16):
            self._username = username
    username = property(get_username, set_username)

    def results(self):
        all_results = []
        for result in Result.all:
            if result.player == self:
                all_results.append(result)
        return all_results 
        return [result for result in Result.all if result.player == self]
    
    def games_played(self):
        all_games = []
        for result in self.results():
            if result.game == self:
                all_games.append(result.game)
        return all_games
        
    # def played_game(self, game):
    #     for self.results 

    def num_times_played(game):
        pass

    def add_result(self, game, score):
        Result(self, game, score)