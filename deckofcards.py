#################### BlackJack Project ####################
# Pham - 2023-12-27
# create deck of card resemblance to the blackjack
# import rules and logo 
###########################################################

logo_rules = ('''
      
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

######################## Blackjack House Rules ########################
      -- There are no Jokers.
      -- Jack/Queen/King all count as 10.
      -- Ace can count as 11 or 1.
      -- the following list as the deck of cards:
        [ A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
#######################################################################
      ''')

# the first set initial the card
cards = {
    1 : "A",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "10",
    11 : "J",
    12 : "Q",
    13 : "K"
    }

# the second set initial the value of the card
cards2 = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
    }
