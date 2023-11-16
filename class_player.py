# Define a class named 'Player'
class Player():
    # Constructor (__init__) method to initialize player attributes
    def __init__(self, name, post, club, nationality, ovr):
        self.name = name
        self.post = post
        self.club = club
        self.nationality = nationality
        self.ovr = ovr
    
    # Method to display information about the player
    def info(self):
        print("{} plays as a {} with {}. His overall rating is {}, and he is {}.".format(self.name, self.post, self.club, self.ovr, self.nationality))

# Create instances of the Player class
player1 = Player("Kevin De Bruyne", "CM", "Manchester City", "Belgian", 91)
player2 = Player("Lionel Messi", "CF", "Inter Miami", "Frenchian", 90)
player3 = Player("Karim Benzema", "CF", "Al Ittihad", "Frenchian", 90)

# Display information about each player
player1.info()
player2.info()
player3.info()
