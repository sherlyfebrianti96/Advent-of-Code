# Read the files for the Input
with open('./Day-02.input.txt') as f:
    bulk = f.read()
    # print(bulk)

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


# store the score value
class Score():
    lost = 0
    draw = 3
    won = 6


class Game:
    def __init__(self, player1, player2):
        self.player1 = Player(player1, 'A', 'B', 'C')
        self.player2 = Player(player2, 'X', 'Y', 'Z')

    def play(self, playRound):
        shakesResult = playRound.split(' ')

        for result in shakesResult:

            if ((result == self.player1.rock()) or (result == self.player1.paper()) or (result == self.player1.scissor())):
                self.player1.play(result)
            else:
                self.player2.play(result)

    def result(self):
        player1Rock = self.player1.selection() == self.player1.rock()
        player1Paper = self.player1.selection() == self.player1.paper()
        player1Scissor = self.player1.selection() == self.player1.scissor()
        player2Rock = self.player2.selection() == self.player2.rock()
        player2Paper = self.player2.selection() == self.player2.paper()
        player2Scissor = self.player2.selection() == self.player2.scissor()

        player1Win = (player1Rock & player2Scissor) | (
            player1Paper & player2Rock) | (player1Scissor & player2Paper)

        player2Win = (player2Rock & player1Scissor) | (
            player2Paper & player1Rock) | (player2Scissor & player1Paper)

        if player1Win:
            self.player1.addScore(Score.won)
            self.player2.addScore(Score.lost)
            return
        elif player2Win:
            self.player1.addScore(Score.lost)
            self.player2.addScore(Score.won)
            return
        else:
            self.player1.addScore(Score.draw)
            self.player2.addScore(Score.draw)
            return


game = Game('Another Elves', 'You')

print('\n------------')
print('Start Game')

for roundCount, playRound in enumerate(playRounds):
    print('\n------------')
    print('Start Round ', roundCount + 1, '\n')

    game.play(playRound)

    # Get result
    game.result()


###############
# Part 2
class Game2:
    def __init__(self, player1, player2):
        self.player1 = Player(player1, 'A', 'B', 'C')
        self.player2 = Player(player2, 'X', 'Y', 'Z')

    def play(self, playRound):
        shakesResult = playRound.split(' ')

        player1ShakesResult = ''
        player2ShakesResult = ''

        for result in shakesResult:
            if ((result == self.player1.rock()) or (result == self.player1.paper()) or (result == self.player1.scissor())):
                player1ShakesResult = result
            else:
                player2ShakesResult = result

        self.player1.play(player1ShakesResult)

        # Part 2 : Outsmart player 1
        # Change the player's 2 movement based on the player1's previous movement

        if player2ShakesResult == self.player2.rock():
            expectedResult = Score.lost
        elif player2ShakesResult == self.player2.paper():
            expectedResult = Score.draw
        elif player2ShakesResult == self.player2.scissor():
            expectedResult = Score.won

        # Change the movement used for the player2
        player1Rock = self.player1.selection() == self.player1.rock()
        player1Paper = self.player1.selection() == self.player1.paper()
        player1Scissor = self.player1.selection() == self.player1.scissor()

        match expectedResult:
            case Score.lost:
                if player1Rock:
                    self.player2.play(self.player2.scissor())
                elif player1Paper:
                    self.player2.play(self.player2.rock())
                elif player1Scissor:
                    self.player2.play(self.player2.paper())
            case Score.draw:
                if player1Rock:
                    self.player2.play(self.player2.rock())
                elif player1Paper:
                    self.player2.play(self.player2.paper())
                elif player1Scissor:
                    self.player2.play(self.player2.scissor())
            case Score.won:
                if player1Rock:
                    self.player2.play(self.player2.paper())
                elif player1Paper:
                    self.player2.play(self.player2.scissor())
                elif player1Scissor:
                    self.player2.play(self.player2.rock())
            case other:
                pass

    def result(self):
        player1Rock = self.player1.selection() == self.player1.rock()
        player1Paper = self.player1.selection() == self.player1.paper()
        player1Scissor = self.player1.selection() == self.player1.scissor()
        player2Rock = self.player2.selection() == self.player2.rock()
        player2Paper = self.player2.selection() == self.player2.paper()
        player2Scissor = self.player2.selection() == self.player2.scissor()

        player1Win = (player1Rock & player2Scissor) | (
            player1Paper & player2Rock) | (player1Scissor & player2Paper)

        player2Win = (player2Rock & player1Scissor) | (
            player2Paper & player1Rock) | (player2Scissor & player1Paper)

        if player1Win:
            self.player1.addScore(Score.won)
            self.player2.addScore(Score.lost)
            return
        elif player2Win:
            self.player1.addScore(Score.lost)
            self.player2.addScore(Score.won)
            return
        else:
            self.player1.addScore(Score.draw)
            self.player2.addScore(Score.draw)
            return


game2 = Game2('Another Elves', 'You')

print('\n\n------------\n')
print('Start Game2')

for roundCount, playRound in enumerate(playRounds):
    print('\n------------')
    print('Start Round ', roundCount + 1, '\n')

    game2.play(playRound)

    # Get result
    game2.result()
