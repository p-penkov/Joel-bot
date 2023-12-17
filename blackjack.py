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

def play_blackjack(num_players):
    random.shuffle(deck)  # Shuffle the deck for a new game

    players = []
    for i in range(num_players):
        name = input(f"Enter the name for player {i+1}: ")
        players.append({'name': name, 'hand': []})

    for _ in range(2):
        for player in players:
            deal_cards(deck, player['hand'])

    dealer_hand = []
    deal_cards(deck, dealer_hand)

    for player in players:
        while True:
            print(f'Player: {player["name"]}')
            print(f'Player hand: {player["hand"]} ({calculate_hand_value(player["hand"])})')
            print(f'Dealer hand: [{dealer_hand[0]}, <face down>]')

            if calculate_hand_value(player["hand"]) > 21:
                print('Player busts!')
                break
            elif calculate_hand_value(player["hand"]) == 21:
                print('Player wins!')
                break

            action = input(f'{player["name"]}, do you want to hit(h) or stand(s)? ')

            if action.lower() == 'h':
                deal_cards(deck, player["hand"])
            else:
                break

    print(f'Dealer hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})')

    if calculate_hand_value(dealer_hand) > 21:
        print('Dealer busts! Players win!')
    else:
        for player in players:
            if calculate_hand_value(player["hand"]) > 21:
                print(f'{player["name"]} busts!')
            elif calculate_hand_value(player["hand"]) > calculate_hand_value(dealer_hand):
                print(f'{player["name"]} wins!')
            elif calculate_hand_value(player["hand"]) < calculate_hand_value(dealer_hand):
                print('Dealer wins!')
            else:
                print('Push!')

while True:
    num_players = int(input('Enter the number of players: '))
    play_blackjack(num_players)
    play_again = input('Do you want to play another game? (yes/no) ')
    if play_again.lower() != 'y' and play_again.lower() != 'yes':
        break
