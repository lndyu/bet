# Event class. Contains specific types of events. Might be useful later.
import datetime
class Event:
    def __init__(self, description, parties ) :
       #status goes from 0 ("in progress" aka results are not out yet) to 1 ("we know who won")
       self.event_status = 0
       self.time = datetime.datetime.now()
       self.parties = []
       self.event = event
    
    # Update stats after completion of event
    def update_status(self) :
       self.event_status = 1

    #
    def 


