# Profile in the obvious sense
import datetime
class Profile:
    users = 0
    def __init__(self, first_name, last_name, dob, identifier): 
        # backend information
        self.identifier = identifier # We need to implement some sort of hash token for unique identification of users
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.joined = datetime.datetime.now()


        # functionality related information
        self.friends = []
        self.feed = [] 
        self.archive = [] # for completed events
        self.stats = Stats(self)

        # Profile class shit
        Profile.users += 1

    # Adds friends to friend list
    def add_friend(self, friend):
        self.friends.append(friend)

    # Removes friends from friend list
    def remove_friend(self, friend):
        self.friends.remove(friend)

    # Adds event to feed 
    def add_event(self, event):
        self.feed.append(event)

    # Removes event from feed 
    def remove_event(self, event):
        self.feed.remove(event)
        
    # Updates Feed
    def update_feed(self) :
        for event in self.feed: # When a user swipes down or some shit we'll update the feed
            event.update_status()
   

