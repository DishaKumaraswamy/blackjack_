import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)>21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score, computer_score):
    
    if user_score == computer_score :
         print("Draw")

    elif computer_score == 0:
        print("Lose, opponent has Blackjack")

    elif user_score == 0:
        print("Win, with a Blackjack")

    elif user_score > 21:
        print("You went over. You Lose")

    elif computer_score > 21:
        print("Opponent went over. You Win")

    elif user_score > computer_score :
        print("You Win")

    else:
        print("You Lose")

def play():
    
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over :
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards : {user_cards}, current score = {user_score}")
        print(f" Computer's card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            
        else:
            repeat = input("Type 'y' to get another card, type 'n' to pass ")
            if repeat == 'y' :
                user_cards.append(deal_cards())

            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand : {user_cards}, final score = {user_score}")
    print(f" Computer's final hand : {computer_cards}, final score = {computer_score}")

    compare_score(user_score, compare_score)

while input("Do you want to play the BlackJack game type 'y', type 'n' otherwise") == 'y' :
    play()
    

