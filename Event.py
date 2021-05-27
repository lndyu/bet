# Event class. Contains specific types of events.
import datetime
class Event:
    def __init__(self, description) :
       self.event_status = "In Progress..."
       self.time = datetime.datetime.now()
       self.parties = {}
       self.description = description

   # Invite person to event
   def invite_person(self, event, profile):
      profile.add_event(event)
      self.add_person(profile)

   # updates status of event
   def update_status(self) :
      if self.status == "In Progress":
         RETRIEVE EVENT OBJECT FROM DATABASE
      elif self.status == "Completed":
         for person in self.parties: # moves event from feed to archive once completed
            person.archive.append(person.feed.pop(self))
         return
      else:
         raise ValueError("Leo lame as fucckk")
       

   # Adds person to event 
   def add_person(self, profile, accepted=0): # Default state of accepted should be zero. An optional argument might come in handy later
      self.parties[profile] = accepted
   
   # Removes person from event
   def remove_person(self, profile):
      profile.feed.pop(profile)
      self.parties.pop(profile)

   def feed_event(self, profile) :
      # When an event is being displayed from the feed, 0 should correspond to a user prompt system in the frontend
      # 1 should correspond to the current information about the event
      if self.parties[profile] == 0:
         self.display_choices()
      elif self.parties[profile] == 1:
         self.display_info()
      else :
         raise ValueError("leo lame")
         

   


