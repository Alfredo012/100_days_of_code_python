import random

#   Rock wins against scissors.
#   Scissors win against paper.
#   Paper wins against rock.

rock = '''
    _ _ _ _ _ _    
---'    _ _ _ _)
        (_ _ _)
        (_ _ _)
----'_ _(_ _)

'''

paper = '''
    _ _ _ _    
---'    _ _ )_
        _ _ _ _)
        _ _ _ _)
----'_ _ _ _ _)

'''

scissors = '''
    _ _ _ _ _   
---'      _ _ )
        '/_ _ _ 
        '_ _ _ _)
----'_ _ )

'''
options = [rock, paper, scissors]

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Logic of the user hand
if user_option == 0 :
    user_hand = rock

elif user_option == 1 :
    user_hand = paper

elif user_option == 2 :
    user_hand = scissors

else :
    print("Invalid option")

#   Logic of the computer hand
computer_hand = random.choice(options)

#   Logic of the game

print("You choose")
print(user_hand)
print("")
print("The computer choose")
print(computer_hand)
print("")

if user_hand == computer_hand :
    print("Tie")

elif user_hand == rock and computer_hand == scissors :
    print("You win")

elif user_hand == scissors and computer_hand == paper :
    print("You win")

elif user_hand == paper and computer_hand == rock :
    print("You win")

elif computer_hand == rock and user_hand == scissors :
    print("The computer win")

elif computer_hand == scissors and user_hand == paper :
    print("The computer win")

elif computer_hand == paper and user_hand == rock :
    print("The computer win")
