############### Blackjack Project #####################

# The deck is of unlimited in size, which means
# that it can contain an infinite number of cards.
# So, the cards in the list have equal probability of being drawn.

# There are no jokers.


# The Ace can count as 11 or 1.
# The score of the ace is 11 if the total score is less than or equal to 21, otherwise it is 1.

# The code

# Importing modules
import random
import os
from art import logo

# The Jack/Queen/King all are counted as 10.
J = Q = K = 10


def deal_card():
    # Returns a random card from the deck.
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Takes a list of our cards and returns the score calculated from the cards

    # Classic Black Jack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You lose 😭"
    elif computer_score > 21:
        return "You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)

    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Score check after dealing a card
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}.\n Your Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # If the game has not ended, the user will be asked if they want to draw another card. If yes, the deal_card() function is used to add another card to the user_cards list. If no, then the game is over.
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done with his play, it's the time for the computer to play. The computer will keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}.\n Your final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Function used to ask if we need to play another game. If the answer is yes, the program clears the console and starts a new game of BlackJack.
while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y":
    os.system("CLS")
    play_game()
