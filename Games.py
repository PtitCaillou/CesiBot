import random

dealer = None

class Dealer():
    instance = None
    
    cards_values = {
        'R' : 13,
        'D' : 12,
        'V' : 11,
        '10': 10,
        '9' : 9,
        '8' : 8,
        '7' : 7,
        '6' : 6,
        '5' : 5,
        '4' : 4,
        '3' : 3,
        '2' : 2,
        '1' : 1
    }
    
    deck = ['R :hearts:','R :spades:', 'R :diamonds:', 'R :clubs:', 
            'D :hearts:', 'D :spades:', 'D :diamonds:', 'D :clubs:', 
            'V :hearts:', 'V :spades:', 'V :diamonds:', 'V :clubs:', 
            '10 :hearts:', '10 :spades:', '10 :diamonds:', '10 :clubs:', 
            '9 :hearts:', '9 :spades:', '9 :diamonds:', '9 :clubs:', 
            '8 :hearts:', '8 :spades:', '8 :diamonds:', '8 :clubs:', 
            '7 :hearts:', '7 :spades:', '7 :diamonds:', '7 :clubs:', 
            '6 :hearts:', '6 :spades:', '6 :diamonds:', '6 :clubs:', 
            '5 :hearts:', '5 :spades:', '5 :diamonds:', '5 :clubs:', 
            '4 :hearts:', '4 :spades:', '4 :diamonds:', '4 :clubs:', 
            '3 :hearts:', '3 :spades:', '3 :diamonds:', '3 :clubs:', 
            '2 :hearts:', '2 :spades:', '2 :diamonds:', '2 :clubs:', 
            '1 :hearts:', '1 :spades:', '1 :diamonds:', '1 :clubs:'
           ]
    
    class __Dealer():
        def __init__(self):
            self.deck = Dealer.deck

    def __new__(c):
        if not Dealer.instance:
            Dealer.instance = Dealer.__Dealer()
            return Dealer.instance
        else:
            return None

    def start(self):
        self.shuffle()

    def shuffle(self):
        self.deck = random.sample(Dealer.deck, len(Dealer.deck))
        
    def draw(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

async def _dealer(ctx, message):
    print("zango")