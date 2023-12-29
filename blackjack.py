#################### BlackJack Project ####################
# Pham - 2023-12-27

###########################################################

import random
import deckofcards

print(deckofcards.logo_rules)
print("Welcome to Blackjack!!! Please read the rules above and let's begin!")

list_of_players = []

def deal(name):
    player = {}
    # generate random number from 1 to 13 which is the total of the number of suite
    first_num = random.randint(1, 13)
    second_num = random.randint(1, 13)
    first_card = deckofcards.cards[first_num]
    second_card = deckofcards.cards[second_num]

    total_count = deckofcards.cards2[first_card] + deckofcards.cards2[second_card]
    if first_card == "A" and second_card == "A":
        total_count = total_count - 10

    player['Name'] = name
    player['Cards'] = f"[{first_card}]", f"[{second_card}]"
    player['total Count'] = total_count

    list_of_players.append(player)

    return f"[{first_card}][{second_card}]"

# add new player each times
def add_player():
    player_name = input("Player Name: ")
    deal(player_name)

def display_players():
    dealer_hand = len(list_of_players) - 1
    print(f"{list_of_players[dealer_hand]['Name']}: {list_of_players[dealer_hand]['Cards'][0]}[]")

    for x in range(0, dealer_hand):
        print(f"{list_of_players[x]['Name']}: {list_of_players[x]['Cards'][0]}{list_of_players[x]['Cards'][1]}")

# loop statement until no more player is added
is_true = True
while is_true:
    add_player()
    yes_no = input("Is there another player: Yes(y) or No(n) ")

    if yes_no == "n":
        deal("Dealer")
        is_true = False
    else:
        is_true = True

display_players()
print(list_of_players)