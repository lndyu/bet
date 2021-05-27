# Contains general stats, as well as trust system
class Stats:
    def __init__(self, profile):
        self.profile = profile 

        self.bets = 0 
        self.cap = 0
        self.won = 0

        self.arbitrations = 0

    # Calculates honest bet rate 
    def calculate_bet_trust(self):
        return round(1 - (self.cap / self.bets), 2) 

    # Return number of arbitrations
    def get_arbitrations(self) :
        return self.arbitrations   

    # Calculates win rate   
    def calculate_win_rate(self) :
        return round(self.won / self.bets, 2)
    
    # Update bet stats after completion of event, should only be called after the completion of the event
    def update_bet_stats(self, won, arbitrators, capped):
        if capped: # capped is boolean representing whether the user was fair
            self.cap += 1
        else : # if its not capped, we will update stats accordingly.
            self.bets += 1
            if self in won:
                self.won += 1
            if self in arbitrators:
                self.arbitrations += 1
