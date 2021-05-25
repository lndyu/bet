# Profile in the obvious sense
import datetime
class Profile:
    users = 0
    def __init__(self, name, dob, username):
        self.username = username
        self.name = name
        self.dob = dob
        self.joined = datetime.datetime.now()
        self.friends = []
        self.feed = [] # this needs to be dynamically retrieved, we can't display the entire list on demand
        self.trust = Trust(self)

        Profile.users += 1

    # Adds friends to friend list, need to implement an accept/decline system as well
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
        

