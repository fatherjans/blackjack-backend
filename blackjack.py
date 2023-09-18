import p1_random as p1   # Import the p1_random module

def main():
    rng = p1.P1Random()   # Create P1Random variable

    # ------------------------VARIABLES----------------------
    game_continue = 0
    game_num = 0    # Records the number of games the player will play
    player_wins = 0     # Tracks number of games player wins
    dealer_wins = 0     # Tracks number of games dealer wins
    tie_games = 0   # Tracks number of games tied between player and dealer

    # ----------------------CARD ASSIGNMENTS------------------------
    ace_card = 'ACE'

    # ------------------------GAME START-----------------------
    while game_continue < 1:    # When the game is played
        game_num += 1   # Increase the game number by one
        print(f"START GAME #{game_num}")    # Print current game number
        new_game = 0    # Tracks when game is a new game
        player_hand = 0     # Tracks player card score for current game
        # Automatically deal card to player
        card = rng.next_int(13) + 1     # Generates a random number in exclusive range [1,13]

        # --------------------------GENERATED CARD VALUES------------------------
        if card > 10:   # If random card is a face card, it will add 10 to the player's score
            player_hand += 10
        else:
            player_hand += card     # Else, card value generated < 10, this card value is added to player's score
        reload_options = 0  # Tracks if we need to reload player's score

        # ------------------------GAME START--------------------
        while new_game == 0:

            # --------------------------DISPLAY CARD VALUES--------------------
            if reload_options == 0:
                if card == 1:
                    print(f'\nYour card is a {ace_card}!')  # Displays ACE card name if card = 1
                elif card > 10:
                    if card == 11:
                        print(f'\nYour card is a JACK!')    # Displays JACK card name if card = 11
                    elif card == 12:
                        print(f'\nYour card is a QUEEN!')   # Displays QUEEN card name if card = 12
                    elif card == 13:
                        print(f'\nYour card is a KING!')    # Displays KING card name if card = 13
                else:
                    print(f'\nYour card is a {card}!')  # Displays card face value from 2 and 9
                print(f'Your hand is: {player_hand}')

            # -------------------PRINT PLAYER HAND VALUE AFTER INITIAL DRAW----------------------
            if player_hand == 21:
                print("\nBLACKJACK! You win!\n")    # If player hand score is 21, player wins
                player_wins += 1
                new_game += 1
            elif player_hand > 21:
                print("\nYou exceeded 21! You lose.\n")     # If player hand score is over 21, player loses
                dealer_wins += 1
                new_game += 1
            else:
                print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")  # Print menu display options
                reload_options = 0
                option = int(input(f'\nChoose an option: '))    # Ask user for menu option input

                # -------------------------------MENU OPTION 1--------------------------
                if option == 1:
                    card = rng.next_int(13) + 1     # Game generates another random card
                    if card > 10:
                        player_hand += 10   # Game adds 10 if face card
                    else:
                        player_hand += card     # Adds a card number between [2 and 10]

                # ------------------------------MENU OPTION 2----------------------------
                elif option == 2:
                    dealer_hand = rng.next_int(11) + 16     # Generate random number inclusive [16-26]
                    print(f'\nDealer\'s hand: {dealer_hand}')   # Prints dealer hand
                    print(f'Your hand is: {player_hand}')   # Prints player hand

                    if dealer_hand > 21:    # Player wins if dealer goes over 21
                        print("\nYou win!\n")
                        player_wins += 1    # Increase player win by 1
                    elif dealer_hand > player_hand:     # Player lose if dealer is greater
                        print("\nDealer wins!\n")
                        dealer_wins += 1    # Increase dealer win by 1
                    elif dealer_hand == player_hand:    # Dealer and player tie if they have the same score
                        print("\nIt's a tie! No one wins!\n")
                        tie_games += 1      # Increase tie games score by 1
                    else:
                        print("\nYou win!\n")   # Else, player win
                        player_wins += 1    # Increase player win by 1
                    new_game += 1   # Restart game continue loop

                # -------------------------------MENU OPTION 3--------------------------------
                elif option == 3:
                    if player_wins > 0:  # If player has atleast 1 win, divide player wins by game number to get percentage
                        percent_wins = player_wins/ (game_num - 1)
                    else:
                        percent_wins = float(0)  # If no player wins, player win percentage = 0%
                    # Prints current game stats
                    print(f'\nNumber of Player wins: {player_wins}\nNumber of Dealer wins: {dealer_wins}\nNumber of tie games: {tie_games}\nTotal # of games played is: {game_num - 1}\nPercentage of Player wins: {percent_wins:.1%}')
                    reload_options = 1  # Reloads the option menu
                # -------------------------------OPTION 4-----------------------------------------
                elif option == 4:
                    exit()  # Exit the program

                # -----------------------------------OPTION INPUT INVALID-------------------------------
                else:  # If a number outside 1-4 is input, display invalid response message
                    print("\nInvalid input!\nPlease enter an integer value between 1 and 4.")
                    reload_options = 1

if __name__ == '__main__':
    main()