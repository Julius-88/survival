"""
This is a survival game
"""


def choice():
    """
    Presents user with their first choice of leaving the apartment or staying.
    If they press a they will leave apartment, if they press b they will stay.
    """
    action = input('Press "a" to leave your apartment, or "b" to stay: ')
    if action != ' ':
        if action == 'a':
            choice_a()
        elif action == 'b':
            print('b')
        else:
            print('invalid choice, try again')
            choice()
    else:
        print('invalid choice, try again')
        choice()


def choice_a():
    """
    If the user pressed "a" on choice they will be brought here.
    """
    print('You have chosen to leave your apartment.')
    print('Will you look for a weapon before you leave?')
    action = input('Press "a" to look for a weapon, or "b" to leave ')
    if action != ' ':
        if action == 'a':
            print('weapon')
        elif action == 'b':
            print('leave')
        else:
            print('invalid choice, try again')
            choice_a()
    else:
        print('invalid choice, try again')
        choice_a()


def name():
    """
    checks to see if player has entered a name
    """
    player_name = input('What is your name player? ').strip()
    if not player_name and player_name != ' ':
        print('Please enter a name')
        name()
    else:
        print(f'Welcome {player_name}, ')
        print('You have been trapped in your apartment!')
        print('Zombies are attacking your city. What do you do? ')


name()


choice()
