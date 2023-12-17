import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

random.shuffle(deck)

def deal_cards(deck, hand):

    card = deck.pop()
    hand.append(card) 

def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value 

player_hand = []
dealer_hand = []

def play_blackjack():
    random.shuffle(deck)  # Shuffle the deck for a new game

    player_hand.clear()  # Clear player's hand for a new game
    dealer_hand.clear()  # Clear dealer's hand for a new game

    deal_cards(deck, player_hand)
    deal_cards(deck, player_hand)
    deal_cards(deck, dealer_hand)
    deal_cards(deck, dealer_hand)

    while True:
        print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
        print(f'Dealer hand: [{dealer_hand[0]}, <face down>]')

        if calculate_hand_value(player_hand) > 21:
            print('Player busts!')
            break
        elif calculate_hand_value(player_hand) == 21:
            print('Player wins!')
            break

        action = input('Do you want to hit(h) or stand(s)? ')

        if action.lower() == 'h':
            deal_cards(deck, player_hand)
        else:
            break

    print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
    print(f'Dealer hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})')

    if calculate_hand_value(player_hand) > 21:
        print('Player busts!')
    elif calculate_hand_value(dealer_hand) > 21:
        print('Dealer busts! Player wins!')
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print('Player wins!')
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        print('Dealer wins!')
    else:
        print('Push!')

while True:
    play_blackjack()
    play_again = input('Do you want to play another game? (yes/no) ')
    if play_again.lower() != 'y' and play_again.lower() != 'yes':
        break
