name = input('Type your name: ')
print('Welcome',name,'to this adventure')

answer = input('You are on a dirt road, it has come to an end and you cant go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across: ')

    if answer == 'swim':
        print('You swam across the river and were eaten by an alligator')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game')
    else:
        print('Not a valid option, You lose.')

elif answer == 'right':
    answer = input('you come to the bridge, it looks wobbly, do you want to cross it or head back? ')

    if answer == 'back':
        print('You go back and lose')
    elif answer == 'cross':
    
        answer = input('you cross the bridge and meet a stranger. do you want to talk to them (yes/no)? ')

        if answer == 'yes':
            print('you talk to the stranger and won gold. you win')
        elif answer == 'no':
            print('you ignore the strangera and they are offended. you lose.')
    else:
        print('Not a valid option, You lose.')



    print()
else:
    print('Not a valid option, You lose.')

print('thank you for trying', name)