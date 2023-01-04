import random
import art

def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    total = sum(cards)
    if total == 21 and len(cards)== 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def playgame():
    user_cards = []
    computer_cards = []
    game_over = False

    print(art.logo)

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:

        player_total = calculate_score(user_cards)
        computer_total = (calculate_score(computer_cards))  

        print(f"Your cards are {user_cards} which equal {player_total}")
        print(f"Dealers cards are {computer_cards} which equal {computer_total}")

        if player_total == 0 or computer_total == 0 or player_total > 21:
            game_over = True
        else:
            user_deal= input("Would you like another card? y/n: ").lower()
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {player_total}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_total}")
    print(compare(player_total, computer_total))
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        playgame()

playgame()
