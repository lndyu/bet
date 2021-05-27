# Friend request class
class Friend(Event) :
    def __init__(self, description, friender, friendee):
        super().__init__(description)
        self.friender = friender
        self.friendee = friendee
        self.add_person(friender, 1)
        self.add_person(friendee)

    # display info
    def display_info(self):
        DISPLAY YOU WANT TO BE FRIENDS WITH friendee.first_name
        RETRACT?
        
    # display choices
    def display_choices(self): 
        DISPLAY friender.first_name WANTS TO BE FRIENDS WITH YOU
        ACCEPT // DECLINE

