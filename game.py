import random

print('-----------------------Snake Water Gun-----------------------\n')
print('Enter s for Snake, w for Water, g for Gun\n')
choices={'s':1, 'w':2, 'g':3,}

your_choice=input('Enter your choice :').lower()

while your_choice not in choices:
    print('Invalid choice! Please enter s, w, or g')
    your_choice=input('Enter your choice again :')

you=choices[your_choice]
computer_choice=random.randint(1,3)

display_choices={1:'Snake', 2:'Water', 3:'Gun',}

print(f'Your choice : {display_choices[you]}\nComputer choice : {display_choices[computer_choice]}')

if computer_choice==you:
    print('!! Game draw !!')
elif computer_choice==2 and you==1 or \
     computer_choice==1 and you ==3 or \
     computer_choice==3 and you==2:
    print('You won the game')
else:
    print('You lose the game')