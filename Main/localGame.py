class LocalGame:
    def __init__(self):
        self.player1 = "White"
        self.player2 = "Black"
        self.past_moves1 = []
        self.past_scores1 = []
        self.past_moves2 = []
        self.past_scores2 = []
        self.timer1 = 0
        self.timer2 = 0
        self.turn = "White"

    def get_player1(self):
        return self.player1

    def set_player1(self, player1):
        self.player1 = player1

    def get_player2(self):
        return self.player2

    def set_player2(self, player2):
        self.player2 = player2

    def get_past_moves1(self):
        return self.past_moves1

    def set_past_moves1(self, past_moves1):
        self.past_moves1 = past_moves1

    def get_past_scores1(self):
        return self.past_scores1

    def set_past_scores1(self, past_scores1):
        self.past_scores1 = past_scores1

    def get_past_moves2(self):
        return self.past_moves2

    def set_past_moves2(self, past_moves2):
        self.past_moves2 = past_moves2

    def get_past_scores2(self):
        return self.past_scores2

    def set_past_scores2(self, past_scores2):
        self.past_scores2 = past_scores2

    def add_past_move1(self, move):
        self.past_moves1.append(move)

    def add_past_score1(self, score):
        self.past_scores1.append(score)

    def add_past_move2(self, move):
        self.past_moves2.append(move)

    def add_past_score2(self, score):
        self.past_scores2.append(score)
    
    def getTurn(self):
        return self.turn