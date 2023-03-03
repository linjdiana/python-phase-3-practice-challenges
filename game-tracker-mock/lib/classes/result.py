class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def get_player(self):
        return self._player
    
    def set_player(self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
    player = (get_player, set_player)

    def get_game(self):
        return self._game
    
    def set_game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
    game = (get_game, set_game)