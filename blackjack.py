from random import randint
user_choise = -1

cards = randint(1,11)
cards = cards + randint(1,11)

bot = randint(1,11)
bot = bot + randint(1, 11)

if bot < 15:
    bot = bot + randint(1,11)

    
while cards <= 21 or cards >= 21:
    print("Wartość twoich kart to", cards)
    print("0-Stand")
    print("1-Hit")
    user_choise = int(input("Wybierz opcje:"))
    print(" ")

    if cards == 21:
        print("Wygrałeś miałeś", cards, "oczek, a bot miał", bot)
        break
    if cards >= 21:
        print("Przegrałeś, miałeś", cards, "oczek, a bot miał", bot)
        break
    if user_choice == 1:
        cards = cards + randint(1,14)
        #print("Twoje wszytskie karty mają wartość", cards)

        if cards == 21:
            print("Wygrałeś miałeś", cards, "oczek, a bot miał", bot)
            break
        if cards >= 21:
            print("Przegrałeś, miałeś", cards, "oczek, a bot miał", bot)
            break


    if user_choise == 2:
        break
    if bot > cards:
        print("Przegrałeś, miałeś", cards, "oczek, a bot miał", bot)
        break

    if bot < cards:
        print("Wygrałeś miałeś", cards, "oczek, a bot miał", bot)
        break
