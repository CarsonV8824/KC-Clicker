class Game_State:
    def __init__(self):
        self.game_state = {
            "username": "guest",
            "money": 0,
            "money_per_sec": 0, 
            "producers": {
                "39th_street": {"39th street owned": 0, "$PerSec": 1, "cost": 100},
                "The_Paseo": {"The Paseo owned": 0, "$PerSec": 5, "cost": 500}
                
                }
            }
    def default_game_state(self):
        return self.game_state.copy()