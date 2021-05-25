# Contains trust system information
class Trust :
    def __init__(self, profile):
        self.profile = profile 

        self.bets = 0 
        self.cap = 0

        self.arbitrations = 0

    # Calculates honest bet rate 
    def calculate_bet_trust(self):
        return round(1 - (self.cap / self.bets), 2) 

    # Return numbers of arbitrations
    def get_arbitrations(self) :
        return self.arbitrations   
    
    # Update trust after completion of event
    def update_stats(self, event):
        self.bets += 1
        # need to implement events class