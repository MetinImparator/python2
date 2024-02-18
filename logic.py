import random
import configparser

def play_game():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    my_money = int(config['DEFAULT']['MY_MONEY'])
    slot_numbers = list(range(1, 11))

    while True:
        print(f"Your current balance: ${my_money}")
        bet = int(input("Place your bet: "))
        if bet > my_money:
            print("You don't have enough money to place this bet.")
            continue

        selected_slot = int(input("Choose a slot (1-10): "))
        winning_slot = random.choice(slot_numbers)

        if selected_slot == winning_slot:
            print(f"Congratulations! You win ${bet * 2}")
            my_money += bet
        else:
            print(f"Sorry, the winning slot was {winning_slot}. You lose ${bet}")
            my_money -= bet

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Game over! Your final balance is ${my_money}")

if __name__ == "__main__":
    play_game()

