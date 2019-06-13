
# coding: utf-8

# In[ ]:


import string
import os
import random
import nltk


# In[ ]:


def is_question(input_string):
    #Check if the input is a question.
       
    #input_string : string
    #String that may contain '?'.
        
    
    if "?" in input_string:
        output = True
    else:
        output = False
    return output 


# In[ ]:


def remove_punctuation(input_string):
    #Remove the punctuations in input string.

    
    out_string =''
    for char in input_string:
        if not char in string.punctuation:
            out_string = out_string + char
    
    return out_string


# In[ ]:


def prepare_text(input_string):
    #Convert all the inputs to lower case string without any punctuations. 

    output_list : list
    #List that contains all the lower case splited words of the input.
    out_list=[]
    
    # Convert strings to lower case letters
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    
    # Split out the words from the string and list them as items in a list
    out_list = temp_string.split()
    return out_list


# In[ ]:


def respond_echo(input_string, number_of_echoes, spacer):
#Repeat input several times.
   
#String to repeat the input by the number of echos with a spacer as separator.

    
    if not input_string == None:
        echo_output = (input_string+spacer)*number_of_echoes
    else:
        echo_output = None

    return echo_output


# In[ ]:


def selector(input_list, check_list, return_list):
    #Repeat input several times.
   
    #String to display the result of a random choice in a list given certain conditions met.

    output = None
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
    return output


# In[ ]:


def string_concatenator(string1, string2, separator):
    #Concatenate strings with separators.

    #String to display the result a series of connected inputs. 
  
    output = string1+separator+string2
    return output


# In[ ]:


def list_to_string(input_list, separator):
    #Concatenate items in a list and conver them to a string with separators.
   
    #String to display the result a series of connected item in the input list. 

    
    output = input_list[0]
    for item in input_list[1:]:
        output=string_concatenator(output, item, separator)
    return output


# In[ ]:


def end_chat(input_list):
    #End chat 

    #Boolean assures whether to end chat based on whether the input contains 'quit'.

    
    if 'no' in input_list:
        return True
    elif 'quit' in input_list:
        return True
    else: 
        return False


# In[ ]:


assert callable(end_chat)
assert isinstance(end_chat(['lalalala', 'have a great day!']), bool)
assert end_chat(['nope']) == False


# In[ ]:


GREETINGS_IN = ['morning', 'hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings','blackjack']
GREETINGS_OUT = ['Good Morning! Would you like to play blackjack? (Type Yes or No)', 'Howdy, how about a game of blackjack? (Type Yes or No)']



RESPONSE_IN = ['yes', 'Yes']

COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.",             "Did you know I'm made of code!?",             "Computers are so magical",             "Do you think I'll pass the Turing test?"]

ANSWER_IN = ['q', 'Q', 'quit']
ANSWER_OUT = ['Thank you for playing! See you next time!']


UNKNOWN =  ['We can start another one if you want (Type Yes or No)']

QUESTION = "I'm assuming you want to play a game of blackjack? (Type Yes or No)"


# In[ ]:


import numpy as numpy

deck = 4 * ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
player_score = 0
dealer_score = 0


#Gives out two cards to player and dealer
def deal_cards(deck):
    hand = []
    for i in range(2):
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand

#Calculates the total value of your hand
def total(hand, boolean):
    card_sum = 0
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            card_sum += 10
        elif card == "Ace":
            if card_sum >= 11:
                card_sum += 1
            else:
                card_sum += 11
                            
        else:
            card_sum += int(card)
    return card_sum

#Calculates the dealer's hand
def total_dealer(hand, boolean):
    
    card_sum = 0
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            card_sum += 10
        elif card == "Ace":
            if card_sum >= 11:
                card_sum += 1
            else:
                card_sum += 11
        else:
            card_sum += int(card)
    return card_sum


#Gives the option to draw another card from the deck
def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    hand.append(card)
    deck.append(card)
    return hand

#Asks to play another game
def play_again():
    again = input("Would you like to play again? (Yes/No): ").lower()
    if again == "yes":
        return "yes"
    else:
        return "no"

#Prints out the total sum of each hand
def return_score(d_cards, p_cards):
    
    print ("DEALER: I have a " + str(d_cards) + " for a total of " + str(total_dealer(d_cards, False)))
    print ("DEALER: You have a " + str(p_cards) + " for a total of " + str(total(p_cards, True)))
    
#Checks blackjack before player hits
def blackjack(d_cards, p_cards):
    if total(p_cards, True) == 21 and total_dealer(d_cards, False) == 21:
        return_score(d_cards, p_cards)
        print("Tied!")
        return True
    if total(p_cards, True) == 21:
        return_score(d_cards, p_cards)
        print ("DEALER: Congrats on winning! You got a Blackjack!")
        return True
    elif total_dealer(d_cards, False) == 21:
        return_score(d_cards, p_cards)
        print ("DEALER: Sorry, you lose. I got a blackjack.")
        return True
    return False

#Check if the player or dealer has won
def score(d_cards, p_cards):
    global player_score
    global dealer_score
    
    if total(p_cards, True) == total_dealer(d_cards, False):
        return_score(d_cards, p_cards) 
        print ("It's a tie")
        player_score = player_score + 1
        dealer_score += 1
        print("PLAYER SCORE:" + str(player_score))
        print("DEALER SCORE:" + str(dealer_score))
    elif total(p_cards, True) == 21:
        return_score(d_cards, p_cards)
        print ("DEALER: Congrats on winning! You got a Blackjack!")
        player_score = player_score + 1
        print("PLAYER SCORE:" + str(player_score))
    elif total_dealer(d_cards, False) == 21:
        return_score(d_cards, p_cards)
        print ("DEALER: Sorry, you lose. I got a blackjack.")
        dealer_score = dealer_score + 1
        print("DEALER SCORE:" + str(dealer_score))
    elif total(p_cards, True) > 21:
        return_score(d_cards, p_cards)
        print ("DEALER: Sorry. You busted. You lose.\n")
        dealer_score = dealer_score + 1
        print("DEALER SCORE:" + str(dealer_score))
    elif total_dealer(d_cards, False) > 21:
        return_score(d_cards, p_cards) 
        print ("DEALER: I bust. You win!\n")
        player_score = player_score + 1
        print("PLAYER SCORE:" + str(player_score))
        
    elif total(p_cards, True) < total_dealer(d_cards, False):
        return_score(d_cards, p_cards)
        print ("DEALER: I'm sorry, you're score is lower than mine. You lose.\n")
        dealer_score = dealer_score + 1
        print("DEALER SCORE:" + str(dealer_score))
    elif total(p_cards, True) > total_dealer(d_cards, False):
        return_score(d_cards, p_cards) 
        print ("DEALER: Congratulations! Your score is higher than mine. You win\n")
        player_score = player_score + 1
        print("PLAYER SCORE:" + str(player_score))

#starts the Blackjack game 
def game():
    global player_score
    global dealer_score
    choice = 0
    
    
    print ("DEALER: Welcome! Are you ready to lose??\n")
    d_cards = deal_cards(deck)
    p_cards = deal_cards(deck)
    while choice != "quit":
        print ("DEALER: My cards are " + str(d_cards[0]))
        print ("DEALER: Your cards are " + str(p_cards) + " for a grand total of " + str(total(p_cards, True)))
        checkGame = blackjack(d_cards, p_cards)
        choice = input("DEALER: Would you like to hit, stay, or quit: ").lower()
        
        if checkGame == False:
            while choice == "hit":
                hit(p_cards)
                print ("DEALER: Your cards are " + str(p_cards) + " for a grand total of " + str(total(p_cards, True)))
                if total(p_cards, False) > 21:
                    print("YOU BUST!! DEALER WINS")
                    dealer_score += 1
                    print("DEALER SCORE:" + str(dealer_score))
                    break
                if total(p_cards, False) == 21:
                    print("Congrats you got Blackjack!")
                    choice = "stay"
                    break
                choice = input("DEALER: Would you like to hit, stay, or quit: ").lower()
                 
            
            if choice == "stay":
                while total_dealer(d_cards, False) <= 17:
                    hit(d_cards)
                    
                score(d_cards, p_cards)
            elif choice == "quit":
                print ("Thanks for playing! See you next time!")
                player_score = 0
                dealer_score = 0
        
        
            
        choiceUser = play_again()
        if choiceUser == "no":
            choice = "quit"
        else:
            d_cards = deal_cards(deck)
            p_cards = deal_cards(deck)
        


# In[ ]:


def play_blackjack():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('PLAYER:\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Alrighty then. See you later!'
            chat = False
        

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            outs.append(selector(msg, ANSWER_IN, ANSWER_OUT))
            
            if "yes" in msg:
                game()
            
            if "quit" in msg:
                out_msg = 'Bye!'
                chat = False


            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('DEALER:', out_msg)
       
    
            


# In[ ]:


play_blackjack()


