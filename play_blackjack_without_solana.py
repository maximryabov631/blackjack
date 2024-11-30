import random


def cards():
    all_cards = {
        """
        ┌─────────┐
        │2        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        2│
        └─────────┘
        """: 2,
        """
        ┌─────────┐
        │3        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        3│
        └─────────┘""": 3,
        """
        ┌─────────┐
        │4        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        4│
        └─────────┘""": 4, 
        """
        ┌─────────┐
        │5        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        5│
        └─────────┘""": 5,
        """
        ┌─────────┐
        │6        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        6│
        └─────────┘""": 6,
        """
        ┌─────────┐
        │7        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        7│
        └─────────┘""": 7,
        """
        ┌─────────┐
        │8        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        8│
        └─────────┘""": 8,
        """
        ┌─────────┐
        │9        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        9│
        └─────────┘""": 9,
        """
        ┌─────────┐
        │10       │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │      10 │
        └─────────┘""": 10,
        """
        ┌─────────┐
        │J        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        J│
        └─────────┘""": 10,
        """
        ┌─────────┐
        │Q        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        Q│
        └─────────┘""": 10,
        """
        ┌─────────┐
        │K        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        K│
        └─────────┘""": 10,
        """
        ┌─────────┐
        │A        │
        │         │
        │         │
        │    ♠    │
        │         │
        │         │
        │        A│
        └─────────┘""": 11  #Ace initially counted as 11
    }
    return all_cards

def pick_random_card():
    deck = cards()
    card = random.choice(list(deck.items()))
    return card

def play_game():
    total_value_player = 0  
    players_cards = []  
    ace_adjusted_player = False  #check if we've already adjusted the Ace
    ace_adjusted_dealer = False
    
    total_value_dealer = 0  
    dealer_cards = ''  

    #Dealer picks one card
    card_dealer = pick_random_card() 
    dealer_cards += card_dealer[0] + ' '
    total_value_dealer += card_dealer[1]
    
    print("--------------------------------------------------")
    print(f"Dealer's shown card: {card_dealer[0]}")
    print(f"Dealer's total card value (shown): {total_value_dealer}")
    print("--------------------------------------------------\n")

    #Player picks two cards initially
    for i in range(2):
        card = pick_random_card()  
        players_cards.append(card[0])  
        total_value_player += card[1]  

    print(f"Your cards: {' '.join(players_cards)}")
    print(f"Total card value: {total_value_player}")
    print("--------------------------------------------------")

    #Allow the player to pick more cards if they choose
    while total_value_player < 21:
        choice = input("Do you want to pick another card? (yes/no): ").lower()
        if choice == "yes":
            card = pick_random_card()  
            players_cards.append(card[0])  
            total_value_player += card[1]  
            print(f"Picked card: {card[0]}, Value: {card[1]}")
            print(f"Your cards: {' '.join(players_cards)}")
            print(f"Total card value: {total_value_player}")
            print("--------------------------------------------------")

            #Check if Ace should be counted as 1 instead of 11 if total exceeds 21
            if total_value_player > 21 and "ACE" in players_cards and not ace_adjusted_player:
                total_value_player -= 10  # Convert Ace from 11 to 1
                ace_adjusted_player = True  # Mark that the Ace has been adjusted
                print(f"Adjusting ACE value... New total card value: {total_value_player}")
                print("--------------------------------------------------")
        elif choice == "no":
            break
        else:
            print("Please enter a valid option (yes/no).")
    
    if total_value_player > 21:
        print(f"Your cards value exceded 21: Your Card value = {total_value_player}. Good Luck Next Time!")
        print("--------------------------------------------------")
    elif total_value_player == 21:
        print("Congratulations your value is 21 you won")
        print("--------------------------------------------------")
        
       
    elif total_value_dealer <= 17:

        while total_value_dealer <= 17 or total_value_dealer > total_value_dealer:
            card_dealer = pick_random_card() 
            dealer_cards += card_dealer[0] + ' ' 
            total_value_dealer += card_dealer[1]
    
            print("--------------------------------------------------")
            print(f"Dealer's cards: {dealer_cards}")
            print(f"Dealer's total card value (shown): {total_value_dealer} ")
            print("--------------------------------------------------\n")


            if total_value_dealer > 21 and "ACE" in dealer_cards and not ace_adjusted_dealer:
                total_value_dealer -= 10  # Convert Ace from 11 to 1
                ace_adjusted_dealer = True  # Mark that the Ace has been adjusted
                print(f"Adjusting ACE value... New total Dealer's card value: {total_value_dealer}")
                print("--------------------------------------------------")
    if total_value_dealer > 21:
        print(f"You won because dealer's card's value exceeded 21. His value {total_value_dealer}")
        
        
    else:
        if total_value_dealer > total_value_player:
            print(f"Dealer won because he has more value then you. Dealers value {total_value_dealer} and Players value {total_value_player}")
            print("--------------------------------------------------\n")
        elif total_value_player > total_value_dealer and total_value_player <21 and total_value_player != 21:
            print(f"You won because your cards value is more then dealers. Your cards value {total_value_player}. Dealers cards value {total_value_dealer}")
            print("--------------------------------------------------")
            
            
        elif total_value_dealer == total_value_player:
            print(f"Its a DRAW. You have the same cards value as Dealer {total_value_player} == {total_value_dealer}")
            print("--------------------------------------------------")




    


   
#Start the game
ask_user_if_he_wants_to_play = input("Do you want to play Black Jack? (yes/no): ")
if ask_user_if_he_wants_to_play == "yes":
    play_game()
else:
    print("Maybe next time!")

print("--------------------------------------------------")
again = input("Do you want to play again? (yes/no) ")
if again == "yes":
    while again == "yes":
        play_game()
        again = input("Do you want to play again? (yes/no) ")

    
