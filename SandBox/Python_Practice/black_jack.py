class Card:
    def __init__(self, suit, rank):
        print "Initializing data"
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print (self.suit + self.rank)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return "The hand has %s" % hand_com

    def card_add(self, card):
        self.cards.append(card)

        # Check for aces
        if card.rank == "A":
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            # Don't show first hidden card
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.card[x].draw()

class Deck:
    def __init__(self):
        "Create a deck in order"
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
