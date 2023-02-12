"""
This is a survival game taking place in a zombie outbreak
YOU MUST SURVIVE!
"""
weapons = []


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

    action = input('Press "a" to look for a weapon or "b" to leave: ')
    if action != ' ':
        if action == 'a':
            weapon()
        elif action == 'b':
            leave()
        else:
            print('invalid choice, try again')
            choice_a()
    else:
        print('invalid choice, try again')
        choice_a()


def weapon():
    """
    If the user pressed "a" to look for a weapon on choice_a
    they will be brought here.
    """
    print('You ransack your apartment but all you can find are kitchen knives '
          'and an old baseball bat. '
          'You dont have any way of putting the knife securly on you '
          'and so you must make a choice. ')

    action = input('Press "a" if you take the knife or "b" to take the bat: ')
    if action != ' ':
        if action == 'a':
            print('knife')
        elif action == 'b':
            print('bat')
        else:
            print('invalid choice, try again')
            weapon()
    else:
        print('invalid choice, try again')
        weapon()


def leave():
    """
    If the user pressed "b" to leave apartment in choice_a
    they will be brought here.
    """
    print('You decide that you have no time to waste. '
          'As you open the door to the hallway, you can hear screams and car '
          'alarms trying to compete for your attention. '
          'You look around and see blood and body parts everywhere '
          'But no zombies! You wonder which is the safest route to take ')

    action = input('Press "a" to take the stairs or "b" to take the elevator: ')
    if action != ' ':
        if action == 'a':
            stairs()
        elif action == 'b':
            elevator()
        else:
            print('invalid choice, try again')
            leave()
    else:
        print('invalid choice, try again')
        leave()


def stairs():
    """
    If the user pressed "a" to take stairs in leave
    they will be brought here.
    """
    print('You decide to take the stairs. '
          'As you are running down you can hear strange growling '
          'from downstairs. ')

    action = input('Press "a" to continue down. '
                   '"b" to go upstairs. '
                   '"c" to go back to your apartment. '
                   '"d" to take the elevator: ')
    if action != ' ':
        if action == 'a':
            print('down')
        elif action == 'b':
            stairs_up()
        elif action == 'c':
            choice_b()
        elif action == 'd':
            elevator()
        else:
            print('invalid choice, try again')
            stairs()
    else:
        print('invalid choice, try again')
        stairs()


def stairs_up():
    """
    If the user pressed "b" to go up the stairs in stairs
    they will be brought here.
    """
    print('You decide to take your chances going up the stairs. '
          'As you are going up past the floors above you '
          'zombies hear your steps and start coming after you. '
          'Panicked you go as fast as you can and eventually reach the '
          'doors going to the roof terrace. '
          'You close the door behind you but there is no locking mechanism. ')

    print('All you can do is hold the opposite end of the door. '
          'The zombies overpower you and you have nowhere to go. '
          'You decide its better to jump to your death than to be '
          'eaten alive. You have died! ')
    name()
    choice()


def elevator():
    """
    If the user pressed "b" to take the elevator in leave
    or "d" in stairs they will be brought here.
    """
    print('You decide to take the elevator and continuously '
          'press the button to make it come faster as you '
          'look around for any danger. '
          'As the familiar sound plings you look infront of '
          'you only to find to your horror several zombies '
          'inside! They grab you before you can react and since you '
          'dont have any weapon on you, you cannot defend yourself. '
          'You have been eaten! GAME OVER!')
    name()
    choice()


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

    action = input('Press "a" to turn on the tv or "b" to look at your phone: '
                   '')
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
    player_name = input('What is your name player?: ').strip()
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
