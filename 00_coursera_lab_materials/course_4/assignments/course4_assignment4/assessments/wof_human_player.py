from wof_player import WOFPlayer
class WOFHumanPlayer(WOFPlayer):


    def getMove(self, category, obscured_phrase, guessed):

        output = f""""
             {self.name} has ${self.prize_money}\n
             \n
             Category: {category}
             Phrase: {obscured_phrase}
             Guessed: {guessed}
             
             Guess a letter, phrase, or type 'exit' or 'pass': 
        """""
        return input(output)
