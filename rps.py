import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def New():
    b = input("Play again (Y/N): ")
    if b == "Y" or b == "y":
        game()
    else:
        print("Closing Game!")
        
def game():
    rps = [rock,paper,scissors]
    user = int(input("Enter 1 for rock, 2 for paper, 3 for scissor: "))
    comp = random.randint(1,3)
    print(f"your choice : {rps[user-1]}")
    print(f"comp choice : {rps[comp-1]}")
    if user == 1:
     if comp == 1:
        print("It's a Draw!")
     elif comp == 2:
        print("You Loose!")
     else:
        print("You Win!")
    elif user == 2:
     if comp == 2:
        print("It's a Draw!")
     elif comp == 3:
        print("You Loose!")
     else:
        print("You Win!")
    else:
     if comp == 3:
        print("It's a Draw!")
     elif comp == 1:
        print("You Loose!")
     else:
        print("You Win!")
    New()
    

def tab():
    a = input("Want to start game(Y/N):  ")
    if a == "Y" or a == "y":
        game()
    else:
        print("Closing Game!")
tab()






    

    
