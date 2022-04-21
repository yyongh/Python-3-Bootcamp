import random

suits = ('♥', '♦', '♠', '♣')
ranks = ('2', '3', '4', '5', '6', '7', '8', 
         '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
          '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 20 and self.aces:
            self.value -= 10
            self.aces -= 1         

class Chips:
    def __init__(self,total=100):
#        self.total = 100  # This can be set to a default value or supplied by a user input
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def ask_starting_chips():
    while True:
        try:
            starting_chips = int(input('How many chips do you have?'))
            return starting_chips
        except:
            print('That is not a valid amount.')  
        else:
            break

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bets!'))
        except ValueError:
            print('That is not a valid bet.')
        else:
            if chips.bet > chips.total:
                print(f'Your bet cannot exceed {chips.total}')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input('Hit or stand? h/s')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer is playing')
            playing = False
        else:
            print('Could you try that again?')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer busts!')
    chips.win_bet()
    
def dealer_wins(chips):
    print('Dealer wins!')
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")


# game starts here
playing = True

# Print an opening statement
print('Welcome to Blackjack!')

# Set up the Player's chips
player_chips = Chips(ask_starting_chips())

while True:    
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()
    
    # Inform Player of their chips total 
    print(f"\nYou now have {player_chips.total} chips.")

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n")
    
    while new_game[0].lower() not in ['y','n']:
        new_game = input("Could you try that again?")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
