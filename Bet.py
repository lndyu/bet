# 
class Bet(Event):
    def __init__(self, description):
        super().__init___(description)

        self.won = []
        self.arbitrators = []
        self.stakeholders = {} 

    # Adds arbitrator iff they aren't a stakeholder
    def add_arbitrator(self, profile) :
        if profile not in self.stakeholders:
            self.arbitrators.append(profile)
            REMOVE_OPTION OF BECOMING AN ARBITRATOR
        else :
            SEND NOTIFICATION "You're already a stakeholder"

    # Adds stakeholder iff they aren't an arbitrator   
    def add_stakeholder(self, profile, stake):
        if profile not in self.arbitrators:
            self.stakeholders[profile] = stake # stakeholders is a collection of profile object, string pairs
            REMOVE OPTION OF BECOMING A STAKEHOLDER
        else:
            SEND NOTIFICATION "You're already an Arbitrator"

    # Removes arbitrator. 
    def remove_arbitrator(self, profile) :
        self.arbitrators.remove(profile)
    

    # display info
    def display_info() :
        DISPLAY DESCRIPTION
        DISPLAY STAKEHOLDERS
        DISPLAY ARBITRATORS 

    # display choices
    def display_choices() :
        JOIN
            JOIN AS ARBITRATOR
            JOIN AS STAKEHOLDER
        DECLINE 


