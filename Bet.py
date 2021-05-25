# 
class Bet(Event):
    def __init__(self, description, author):
        super().__init___()
        self.description = description
        self.arbitrators = []
        self.stakeholders = {}
        self.author = author
        self.status = "Planned" # Need a better word for this...like what's before "in progress"

    # Adds arbitrator to list of arbitrators iff they aren't a stakeholder
    def add_arbitrator(self, profile) :
        if profile in self.stakeholders :
            send_notification("cant be a stakeholder and arbitrator") # to be implemented
        else :
            self.arbitrators.append(profile)

    # Removes arbitrator 
    def remove_arbitraotr(self, profile) :
        self.arbitrators.remove(profile)

    # Remove stakeholder
    def remove_stakeholder(self, profile) :
        self.stakeholders.pop(profile)

    # Adds stakeholder to pool and stores their stake
    def add_stakeholder(self, profile, stake):
        self.stakeholders[profile] = stake

    # Gives information about all parties involved, stakes, etc..
    def current_information(self):
        return [self.description, self.stakeholders, self.arbitrators, self.status]
    
    # Invite arbitrator
    def invite_arbitrator(self, profile) :

    # Invite stakeholder
    def invite_stakeholder(self, profile) :
    