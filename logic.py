import random
import configparser

def play_game():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    my_money = int(config['DEFAULT']['MY_MONEY'])
    slot_numbers = list(range(1, 11))

    while True:
        print(f"Ваш текущий баланс: ${my_money}")
        bet = int(input("Сделайте свою ставку: "))
        if bet > my_money:
            print("У вас недостаточно денег, чтобы сделать эту ставку.")
            continue

        selected_slot = int(input("Выберите цифру (1-10): "))
        winning_slot = random.choice(slot_numbers)

        if selected_slot == winning_slot:
            print(f"Поздравляю! Ты выиграл ${bet * 2}")
            my_money += bet
        else:
            print(f"Извините, выигрышный слот был {winning_slot}. Ты проиграл ${bet}")
            my_money -= bet

        play_again = input("Вы хотите продолжить? (Да/нет): ").lower()
        if play_again != 'нет':
            break

    print(f"Игра окончена! Ваш окончательный баланс равен ${my_money}")

if __name__ == "__main__":
    play_game()

