"""
This is a survival game
"""


def choice():
    """
    Presents user with their first choice of leaving the apartment or staying.
    If they press "a" they will leave apartment, if they press "b"
    they will stay.
    """
    action = input('Press "a" to leave your apartment or "b" to stay: ')
    if action != ' ':
        if action == 'a':
            choice_a()
        elif action == 'b':
            choice_b()
        else:
            print('invalid choice, try again')
            choice()
    else:
        print('invalid choice, try again')
        choice()


def choice_a():
    """
    If the user pressed "a" to leave apartment on choice they will be brought
    here.
    """
    print('Filled with adrenaline you have chosen to leave your apartment. '
          'You suddenly realize it might be a good idea to have some '
          'protection. Will you look for a weapon before you leave?')

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


def choice_b():
    """
    If the user pressed "b" to stay on choice they will be brought here.
    """
    print('You have chosen to stay in your apartment. '
          'Congratulations you survived the first night! '
          'You have consumed some of your resources. '
          'You wake up the next day in a haze, a part of you does not want to '
          'believe what has happened. You look around the apartment '
          'and try to decide what to do next. '
          'You can turn on the tv to see the news '
          'or you could look at your phone to see if anyone has called you.')

    action = input('Press "a" to turn on the tv or "b" to look at your phone ')
    if action != ' ':
        if action == 'a':
            print('tv')
        elif action == 'b':
            print('phone')
        else:
            print('invalid choice, try again')
            choice_b()
    else:
        print('invalid choice, try again')
        choice_b()


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
        print('You have been trapped in your apartment! '
              'Zombies are attacking your city. '
              'What do you do? ')


name()


choice()
