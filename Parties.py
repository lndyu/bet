class Parties:
    def __init__(self) :
        #if code for side 1 and 2 corresponds to group 1 and group 2. 3 means arbitrator
        bank = {}
        size = 0
        size_group1 = 0
        size_group2 = 0
        size_group3 = 0

    #adds a damn stakeholder
    def add_stakeholder(self,side,profile,amount):
        #if not arbitrator or already a stakeholder
        bank[profile] = {"amount": amount, "side", side}
        self.size += 1
        if(side == 1):
            self.size_group1 += 1
        elif(side == 2):
            self.size_group2 += 2
    
    #removes a damn stakeholder
    def remove_stakeholder(self,profile):
        #if is stakeholder
        group_number = self.get_side(profile)
        self.bank.pop(profile)
        if(group_number == 1):
            self.size_group1 -= 1
        if(group_number == 2):
            self.size_group2 -= 1
        self.size -= 1


    #adds a damn arbitrator
    def add_arbitrator(self,profile):
        #if not arbitrator or already a stakeholder
        self.bank[profile] = { "side", 3}
        self.size += 1
        self.size_group3 += 1


    #remove a damn arbitrator
    def remove_arbitrator(self,profile):
        #if is arbitrator
        self.bank.pop(profile)
        self.size -= 1
        self.size_group3 -= 1

    #gets the side given profile
    def get_side(self, profile):
        return self.bank[profile]["side"]
    
    #gets the amount given profile
    def get_amount(self, profile):
        return self.bank[profile]["amount"]
    
    #returns if it contains something
    def contains(self,profile):
        return self.bank.contains(profile)
    
    #returns list of all group1
    def first_group(self):
        result = []
        for b in self.bank:
            if self.get_side(b) == 1:
                result.append(b)
        return result

    #returns list of all group2
    def second_group(self):
        result = []
        for b in self.bank:
            if self.get_side(b) == 2:
                result.append(b)
        return result

    #returns list of all group2
    def arbitrators_group(self):
        result = []
        for b in self.bank:
            if self.get_side(b) == 3:
                result.append(b)
        return result
    
    #returns list of all participants
    def all_participants(self):
        return list(self.bank.keys())

    def size_group_1(self):
        return self.size_group1

    def size_group_2(self):
        return self.size_group2

    def size_arbitrators(self):
        return self.size_group3