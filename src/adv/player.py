# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, playerName, currRoom):
    self.room = currRoom
    self.playerName = playerName

    self.contents = []

    self.score = 0
    