# 
class Bet(Event):
    def __init__(self, description, author):
        super().__init___()
        self.description = description
        self.party = Parties()
        self.author = author
        self.winner = -1 #0: undecided, 1 or 2: group 1 or group 2

    # Adds arbitrator to list of arbitrators iff they aren't a stakeholder
    def add_arbitrator(self, profile) :
        self.party.add_arbitrator(profile)

    # Removes arbitrator 
    def remove_arbitrator(self, profile) :
        self.party.remove_arbitrator

    # Remove stakeholder
    def remove_stakeholder(self, profile) :
        self.party.remove_stakeholder(profile)

    # Adds stakeholder to pool and stores their stake
    def add_stakeholder(self, profile, stake, side): #side given by 1 or 2
        self.party.add_stakeholder(side,profile,stake)

    # Gives information about all parties involved, stakes, etc..
    def current_information(self):
        if(self.event_status = 0):
            return [self.description, self.party, "In progress..."]
        elif(self.event_status = 1):
            return [self.description, self.party, self.winner, "Completed"]
    
    # Updates with winner and loser
    def update_results(self,winner): #winner is 1 or 2
        self.winner = winner
        self.update_status()
    
    # Invite arbitrator
    def invite_arbitrator(self, profile) :

    # Invite stakeholder
    def invite_stakeholder(self, profile) :
    