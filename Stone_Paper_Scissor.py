
import random
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='sy':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'sy':
            return True
    elif comp == 'sy':
        if you == 'sy':
            return False
        elif you == 's':
            return True

print('Comp Turn: Stone(s), Paper(p), Scissor(sy)')
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo ==3:
    comp ='sy'

you = input('Your turn: Stone(s), Paper(p), Scissors(s) :')
a = gameWin(comp, you)
print(f'Computer chose {comp}')
print(f'You chose {you}')
 
if a == None:
    print('The game is tie')
elif a:
    print('You win')
else:
    print('You lose')