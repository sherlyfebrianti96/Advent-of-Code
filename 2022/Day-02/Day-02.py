# Read the files for the Input
with open('./Day-02.input.txt') as f:
    bulk = f.read()
    print(bulk)

# Separate each game play rounds
playRounds = bulk.split('\n')


class Player:
    # Create class for the Player object
    def __init__(self, name, rock, paper, scissor):
        self._name = name
        self._rock = rock
        self._paper = paper
        self._scissor = scissor
        self._selection = ''
        self._score = 0

    def play(self, selection):
        self._selection = selection
        print(self._name, ' choose ', self._selection, '\n')

    def addScore(self, score):
        self._score += score

        if (self._selection == self._rock):
            self._score += 1
        elif (self._selection == self._paper):
            self._score += 2
        elif (self._selection == self._scissor):
            self._score += 3

        print(self._name, ' : ', self._score)

    # getter method
    def rock(self):
        return self._rock

    def paper(self):
        return self._paper

    def scissor(self):
        return self._scissor

    def selection(self):
        return self._selection

    def score(self):
        return self._score


# Create a dictionary to store the score value
score = {'lost': 0, 'draw': 3, 'won': 6}

player1 = Player('Another Elves', 'A', 'B', 'C')
player2 = Player('You', 'X', 'Y', 'Z')


class Game:
    def __init__(self, player1, player2):
        player1 = Player(player1, 'A', 'B', 'C')
        player2 = Player(player2, 'X', 'Y', 'Z')

    def play(self, playround):
        shakesResult = playRound.split(' ')

        for result in shakesResult:
            if ((result == player1.rock()) or (result == player1.paper()) or (result == player1.scissor())):
                player1.play(result)
            else:
                player2.play(result)

    def result(self):
        player1Rock = player1.selection() == player1.rock()
        player1Paper = player1.selection() == player1.paper()
        player1Scissor = player1.selection() == player1.scissor()
        player2Rock = player2.selection() == player2.rock()
        player2Paper = player2.selection() == player2.paper()
        player2Scissor = player2.selection() == player2.scissor()

        player1Win = (player1Rock & player2Scissor) | (
            player1Paper & player2Rock) | (player1Scissor & player2Paper)

        player2Win = (player2Rock & player1Scissor) | (
            player2Paper & player1Rock) | (player2Scissor & player1Paper)

        if player1Win:
            player1.addScore(score['won'])
            player2.addScore(score['lost'])
            return
        elif player2Win:
            player1.addScore(score['lost'])
            player2.addScore(score['won'])
            return
        else:
            player1.addScore(score['draw'])
            player2.addScore(score['draw'])
            return


game = Game('Another Elves', 'You')

for roundCount, playRound in enumerate(playRounds):
    print('\n------------')
    print('Start Round ', roundCount + 1, '\n')

    game.play(playRound)

    # Get result
    game.result()
