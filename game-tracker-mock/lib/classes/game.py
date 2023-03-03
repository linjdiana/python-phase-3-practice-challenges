from classes.result import Result

class Game:
    def __init__(self, title):
        self.title = title
    
    def get_title(self):
        return self._title
    def set_title(self, title):
        if isinstance(title, str) and (len(title) > 0) and not hasattr(self, "_title"):
            self._title = title
    title = property(get_title, set_title)

    def results(self):
        return [result for result in Result.all if result.game == self]
    
    def players(self):
        all_players = []
        for result in self.results():
            all_players.append(result.player)
        return all_players
    
    def average_score(self, player):
        results = self.results()
        scores = [result.score for result in results]
        sum_scores = sum(scores)
        num_scores = len(scores)
        return sum_scores / num_scores
