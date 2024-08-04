class LocalGame:
    def __init__(self):
        self.player1 = "White"
        self.player2 = "Black"
        self.target1 = ""
        self.target2 = ""
        self.past_moves1 = []
        self.past_scores1 = []
        self.past_moves2 = []
        self.past_scores2 = []
        self.timer1 = 10
        self.timer2 = 10
        self.turn = "White"

    def get_target1(self):
        return self.target1

    def set_target1(self, target1):
        self.target1 = target1

    def get_target2(self):
        return self.target2

    def set_target2(self, target2):
        self.target2 = target2

    def get_timer1(self):
        return self.timer1

    def set_timer1(self, timer1):
        self.timer1 = timer1

    def get_timer2(self):
        return self.timer2

    def set_timer2(self, timer2):
        self.timer2 = timer2

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
    
    def switchTurn(self):
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"

    def top_ten(self, player):
        if player == "Black":
            guesses = self.past_moves2
            scores = self.past_scores2
        else:
            guesses = self.past_moves1
            scores = self.past_scores1

        # Step 1: Combine guesses and scores into a list of tuples
        combined = list(zip(guesses, scores))

        combined = [(guess, float((score))) for guess, score in combined]
            
        # Step 2: Sort the list by scores in descending order
        combined.sort(key=lambda x: x[1], reverse=True)
            
        # Step 3: Extract the top 10 guesses and scores
        top_guesses = [item[0] for item in combined[:10]]
        top_scores = [item[1] for item in combined[:10]]
            
        # Step 4: Return the two lists
        return top_guesses, top_scores

        