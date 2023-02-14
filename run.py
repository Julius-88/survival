"""
This is a text based survival game taking place in a zombie outbreak
YOU MUST SURVIVE!
"""
import sys
weapons = []
knowledge = []
bag = []


def check_knowledge():
    """
    Checks to see if the player is aware of both
    water and supply
    """
    return 'water' in knowledge and 'supplies' in knowledge


def check_supplies():
    """
    Checks to see if the player has both
    water and supply
    """
    return 'water' in bag and 'supplies' in bag


def check_knowledge_resource():
    """
    Checks to see if the player is aware of either
    water or supply
    """
    return 'water' in knowledge or 'supplies' in knowledge


def border():
    """
    Creates a border of * and spacing so it is easier to see the game text.
    """
    print('\n')
    print('*' * 20)
    print('\n')


def choice():
    """
    Presents user with their first choice of leaving the apartment or staying.
    If they press "a" they will leave apartment, if they press "b"
    they will stay.
    """
    weapons.clear()
    knowledge.clear()
    bag.clear()

    border()
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
    Here the player can choose if they
    wish to search for a weapon before they
    leave
    """
    border()
    print('Filled with adrenaline you have chosen to leave your apartment. '
          'You suddenly realize it might be a good idea to have some '
          'protection. Will you look for a weapon before you leave?')
    border()

    action = input('Press "a" to look for a weapon or "b" to leave: ')
    if action != ' ':
        if action == 'a':
            weapon()
        elif action == 'b' and check_supplies():
            leave()
        elif action == 'b' and 'water' in knowledge:
            print('You gather all the water you can in a bag '
                  'before you leave.')
            bag.append('water')
            leave()
        elif action == 'b' and 'supplies' in knowledge:
            print('You gather all the food you can in a bag '
                  'before you leave.')
            bag.append('supplies')
            leave()
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
    Here the player can choose a weapon.
    """
    border()
    print('You ransack your apartment but all you can find are kitchen knives '
          'and an old baseball bat. '
          'You dont have any way of putting the knife securly on you '
          'and so you must make a choice. ')
    border()

    action = input('Press "a" if you take the knife or "b" to take the bat: ')
    if action != ' ':
        if action == 'a':
            knife()
        elif action == 'b':
            bat()
        else:
            print('invalid choice, try again')
            weapon()
    else:
        print('invalid choice, try again')
        weapon()


def knife():
    """
    Here the player can pick up a knife.
    """
    weapons.append('knife')
    border()
    print('Armed with the biggest knife you could find '
          'you are ready to face what is outside. ')

    if check_supplies():
        leave()
    elif 'water' in knowledge:
        print('You gather all the water you can in a bag '
              'before you leave.')
        bag.append('water')
        leave()
    elif 'supplies' in knowledge:
        print('You gather all the supplies you can in a bag '
              'before you leave ')
    leave()


def bat():
    """
    Here the player can pick up a bat.
    """
    weapons.append('bat')
    border()
    print('Armed with your trusty bat '
          'you are ready to face what is outside. ')

    if check_supplies():
        leave()
    elif 'water' in knowledge:
        print('You gather all the water you can in a bag '
              'before you leave.')
        bag.append('water')
        leave()
    elif 'supplies' in knowledge:
        print('You gather all the supplies you can in a bag '
              'before you leave ')
    leave()


def leave():
    """
    Here the player can choose to leave
    immediately.
    """
    border()
    print('You decide that you have no time to waste. '
          'As you open the door to the hallway, you can hear screams and car '
          'alarms trying to compete for your attention.\n '
          'You look around and see blood and body parts everywhere '
          'But no zombies! You wonder which is the safest route to take. ')
    border()

    action = input('Press "a" to take the stairs or "b" to take the elevator: '
                   '')
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
    Here the player gets to choose
    which direction they wish to go in the staircase.
    """
    border()
    print('As you are running down the stairs you can hear strange growling '
          'from the bottom ')
    border()

    action = input('Press "a" to continue down. '
                   '"b" to go upstairs. '
                   '"c" to go back to your apartment. '
                   '"d" to take the elevator: ')
    if action != ' ':
        if action == 'a':
            stairs_down()
        elif action == 'b':
            stairs_up()
        elif action == 'c':
            border()
            print('Terrified of the outside world, '
                  'you decide to go back to your apartment. '
                  'You quickly run out of resources and decide to '
                  'try and escape but it is to late. '
                  'The zombies fill the hallways and you are quickly '
                  'overwhelmed. You have died! GAME OVER! ')
            border()
            name()
            choice()
        elif action == 'd':
            elevator()
        else:
            print('invalid choice, try again')
            stairs()
    else:
        print('invalid choice, try again')
        stairs()


def stairs_down():
    """
    Here the player can choose what to do when
    they go down the staircase.
    """
    border()
    print('As you continue down the stairs you see two zombies '
          'eating someone right next to the door to the exit. ')
    border()

    action = input('Press "a" to try and sneak past them '
                   '"b" to run past them '
                   '"c" to attack them: ')
    if action != ' ':
        if action == 'a':
            sneak()
        elif action == 'b':
            run()
        elif action == 'c':
            attack()
        else:
            print('invalid choice, try again')
            stairs_down()
    else:
        print('invalid choice, try again')
        stairs_down()


def sneak():
    """
    Here the player can choose to sneak past the zombies.
    """
    border()
    print('You successfully sneak past the zombies and avoid '
          'stepping into any pool of blood. As you open the door '
          'you are greeted by a city in complete chaos. '
          'You know the odds are against you but atleast you got a chance! '
          'Congratulations you survived chapter one! ')
    border()


def run():
    """
    Here the player can choose to run past the zombies.
    """
    border()
    print('As you sprint towards the exit '
          'you slip on a pool of blood '
          'and fall on your back hitting your head. '
          'As you try to collect yourself, your vision returns '
          'to normal only in time to see one of the zombies '
          'quickly approaching your face with an open maw. '
          'You have died! GAME OVER! ')
    border()
    name()
    choice()


def attack():
    """
    Here the player can choose to attack the zombies.
    """
    if 'knife' in weapons and 'kill' in knowledge:
        border()
        print('As you approach the zombies you remember what you '
              'heard in the news and aim for the first zombies '
              'head. Killing it in one blow! You quickly pull out '
              'your knife and stab the other one right through its eyes. '
              'Standing in disbelief of what you have done, you feel '
              'that you are now ready to face the grim reality of the world. ')
        border()
        sys.exit('Congratulations you survived chapter one!')
    elif 'bat' in weapons and 'kill' in knowledge:
        border()
        print('As you prepare to attack the zombies you '
              'remember what they said on the news. '
              'You yell at the zombies and they start to approach you. '
              'As the first one comes close enough, you aim for the head. '
              'A loud cracking sound comes from the zombie as it falls down. '
              'You quickly move towards the other one and hit it on its head. '
              'It too falls down and you start to repeatedly bash its head '
              'until it is cracked. You then move to the first zombie to '
              'finish the job. '
              'You take a deep breath, covered in blood and knowledge '
              'you are ready to face what awaits you outside.')
        border()
        sys.exit('Congratulations you survived chapter one!')
    elif 'knife' in weapons:
        weapons.pop()
        border()
        print('You pull out your knife and stab the closest zombie. '
              'It does not seem to affect them. '
              'They both rise up and start attacking you as you '
              'repeatedly stab them, fighting for your life. '
              'They overwhelm you. You have died! GAME OVER! ')
        border()
        name()
        choice()
    elif 'bat' in weapons:
        weapons.pop()
        border()
        print('You ready your bat and yell at the zombies. '
              'They rise up and start approaching you. '
              'You swing your bat at the closest one hitting its jaw. '
              'The zombie staggers a bit but does not seem to '
              'register the blow and keeps approaching. '
              'You back away and try to swing again, hitting '
              'one of the zombies on the arm. As you do so '
              'you slip on a pool of blood and fall down. '
              'The zombie closest to you grabs your feet '
              'and tries to take a bite. As you try to kick it '
              'off of you, the other zombie has closed in on you '
              'and starts to eat your arm. '
              'You have died! GAME OVER! ')
        border()
        name()
        choice()
    else:
        border()
        print('You engange the zombies in hand to hand combat '
              'it is a futile attempt as they quickly start biting you. '
              'You have died! GAME OVER! ')
        border()
        name()
        choice()


def stairs_up():
    """
    Here the player goes upstairs and can
    see the consequences of their choices.
    """
    border()
    print('You decide to take your chances going up the stairs. '
          'As you are going up past the floors above you '
          'zombies hear your steps and start coming after you. '
          'Panicked you go as fast as you can and eventually reach the '
          'doors going to the roof terrace. '
          'You close the door behind you but there is no locking mechanism. ')

    if 'bat' in weapons and check_supplies():
        weapons.pop()
        bag.clear()
        border()
        print('You quickly use your bat and put it in the door handle '
              'thus preventing it from being open. '
              'With no way out you have no choice but to wait '
              'for rescue. You ration your supplies and '
              'manage to live long enough for a helicopter to spot you. ')
        border()
        sys.exit('Congratulations you survived chapter one!')
    elif 'bat' in weapons:
        weapons.pop()
        border()
        print('You quickly use your bat and put it in the door handle '
              'thus preventing it from being open. '
              'You are now trapped on the roof, with no supplies '
              'or a way out. You starve to death. '
              'You have died! GAME OVER! ')
        border()
        name()
        choice()
    else:
        border()
        print('All you can do is hold the opposite end of the door. '
              'The zombies overpower you and you have nowhere to go. '
              'You decide its better to jump to your death than to be '
              'eaten alive. You have died! GAME OVER! ')
        border()
        name()
        choice()


def elevator():
    """
    Here the player can see the consequences of their choices.
    """
    border()
    print('You decide to take the elevator and continuously '
          'press the button to make it come faster as you '
          'look around for any danger. '
          'As the familiar sound plings you look infront of '
          'you only to find to your horror several zombies '
          'inside! They grab you before you can react '
          'You have been eaten! GAME OVER!')
    border()
    name()
    choice()


def choice_b():
    """
    Here the player can choose what to do in their apartment.
    """
    border()
    print('You have chosen to stay in your apartment. '
          'You can turn on the tv to see the news '
          'or you could look at your phone to see if anyone has called you.')
    border()

    action = input('Press "a" to turn on the tv or "b" to look at your phone: '
                   '')
    if action != ' ':
        if action == 'a':
            watch_tv()
        elif action == 'b':
            watch_phone()
        else:
            print('invalid choice, try again')
            choice_b()
    else:
        print('invalid choice, try again')
        choice_b()


def watch_phone():
    """
    Here the player uses his phone and has to decide what to
    do with the new information he has been given.
    """
    border()
    print('You open your phone and see that you have several missed calls '
          'and voice messages from family and friends. '
          'You try to call them back but the lines are down. '
          'You start listening to the voice messages and '
          'get information about where your friends are headed, '
          'panic strikes you though, as you hear your mothers voice. '
          'She is locked inside her villa in the suburbs and your father '
          'has not come home. She is alone and afraid and fears the '
          'worst has happened to your father. ')
    border()

    knowledge.extend(['friend', 'family'])

    if 'kill' in knowledge and check_knowledge_resource():
        if 'water' in knowledge:
            action = input('Press "a" to leave your apartment '
                           'and go to your mother. '
                           '"b" to leave your apartment and go to your '
                           'friends. '
                           '"e" to gather your supplies. ')
        else:
            action = input('Press "a" to leave your apartment '
                           'and go to your mother. '
                           '"b" to leave your apartment and go to your '
                           'friends. '
                           '"d" to gather your water: ')
    else:
        action = input('Press "a" to leave your apartment '
                       'and go to your mother. '
                       '"b" to leave your apartment and go to your friends. '
                       '"c" to watch tv. ')
    if action != ' ':
        if action in ('a', 'b') and check_knowledge():
            border()
            print('You gather all the water and supplies you can '
                  'and put it in a bag '
                  'before you leave. ')
            bag.append('supplies')
            bag.append('water')
            choice_a()
        elif action in ('a', 'b'):
            leave()
        elif action == 'c' and 'kill' not in knowledge:
            watch_tv()
        elif action == 'd' and 'water' not in knowledge:
            water()
        elif action == 'e' and 'supplies' not in knowledge:
            supplies()
        else:
            print('invalid choice, try again')
            watch_phone()
    else:
        print('invalid choice, try again')
        watch_phone()


def watch_tv():
    """
    Here the player gains insight on what is going on
    in the world. They must now decide how to proceed.
    """
    border()
    print('You turn on the tv and you are immediatly greeted '
          'by the emergency broadcast system. '
          'It seems to be on repeat. '
          '"If you are watching this, a great disaster has occured. '
          'The dead have risen and are attacking the living! '
          'Although we do not know why this is happening. We are '
          'working on a solution. Stay in your homes until military forces '
          'can reach you. Until then here are some guidelines. '
          '1. Collect as much water as you can from the tap. '
          '2. Ration your food, be prepared to wait for a long period. '
          '3. If you have to fight them, damage the brain, '
          'it is the only way to kill them. '
          'If you are bitten you will turn into one of them. '
          'Be careful, be safe and may god be with you." '
          'You sit down on your couch as if all air has left your body. '
          'You try to process what the message is saying '
          'and start thinking of your options. ')
    border()

    knowledge.append('kill')

    if 'family' in knowledge:
        action = input('Press "b" to gather as much water as you can. '
                       '"c" to gather your supplies. '
                       '"d" to leave your apartment '
                       'and go to your mother. '
                       '"e" to leave your apartment and go to your friends. ')
    else:
        action = input('Press "a" to check on your phone '
                       '"b" to gather as much water as you can '
                       '"c" to gather your supplies: ')
    if action != ' ':
        if action == 'a' and 'family' not in knowledge:
            watch_phone()
        elif action == 'b':
            water()
        elif action == 'c':
            supplies()
        elif action in ('d', 'e') and 'family' in knowledge:
            leave()
        else:
            print('invalid choice, try again')
            watch_tv()
    else:
        print('invalid choice, try again')
        watch_tv()


def water():
    """
    Here the player gathers as much water as possible for their survival.
    """
    border()
    print('You search your apartment for any '
          'containers you can find.\n '
          'Once you have found everything you had, '
          'you start filling them with tap water. '
          'Once you are done, you look around thinking of what to do next. ')
    border()
    knowledge.append('water')

    if 'family' not in knowledge and 'supplies' not in knowledge:
        action = input('Press "a" to check on your phone '
                       '"c" to gather your supplies: ')
    elif 'family' not in knowledge:
        action = input('Press "a" to check on your phone: ')
    elif check_knowledge():
        action = input('Press "d" to leave your apartment '
                       'and go to your mother. '
                       '"e" to leave your apartment and go to your friends. ')
    else:
        action = input('Press "d" to leave your apartment '
                       'and go to your mother. '
                       '"e" to leave your apartment and go to your friends. '
                       '"c" to gather your supplies: ')
    if action != ' ':
        if action == 'a' and 'family' not in knowledge:
            watch_phone()
        elif action == 'c' and 'supplies' not in knowledge:
            supplies()
        elif action in ('d', 'e') and check_knowledge():
            border()
            print('You gather all the water and supplies you can '
                  'and put it in a bag '
                  'before you leave. ')
            bag.append('supplies')
            bag.append('water')
            choice_a()
        elif action in ('d', 'e'):
            border()
            print('You gather all the water you can '
                  'and put it in a bag '
                  'before you leave. ')
            bag.append('water')
            choice_a()
        else:
            print('invalid choice, try again')
            water()
    else:
        print('invalid choice, try again')
        water()


def supplies():
    """
    Here the player gathers all the supplies they have in their apartment.
    """
    border()
    print('You search your apartment for any '
          'supplies that can be of use. '
          'You gather it all in one place.\n '
          'Once you are done, you look around thinking of what to do next. ')
    border()
    knowledge.append('supplies')

    if 'family' not in knowledge and 'water' not in knowledge:
        action = input('Press "a" to check on your phone '
                       '"c" to gather your water: ')
    elif 'family' not in knowledge:
        action = input('Press "a" to check on your phone: ')
    elif check_knowledge():
        action = input('Press "d" to leave your apartment '
                       'and go to your mother. '
                       '"e" to leave your apartment and go to your friends: ')
    else:
        action = input('Press "d" to leave your apartment '
                       'and go to your mother. '
                       '"e" to leave your apartment and go to your friends. '
                       '"c" to gather your water: ')
    if action != ' ':
        if action == 'a' and 'family' not in knowledge:
            watch_phone()
        elif action in ('d', 'e') and check_knowledge():
            border()
            print('You gather all the supplies and water '
                  'you can and put it in a bag '
                  'before you leave. ')
            bag.append('supplies')
            bag.append('water')
            choice_a()
        elif action == 'c' and 'water' not in knowledge:
            water()
        elif action in ('d', 'e'):
            border()
            print('You gather all the supplies you can '
                  'and put it in a bag. '
                  'before you leave. ')
            bag.append('supplies')
            choice_a()
        else:
            print('invalid choice, try again')
            supplies()
    else:
        print('invalid choice, try again')
        supplies()


def name():
    """
    checks to see if player has entered a name
    """
    player_name = input('What is your name player?: ').strip()
    if not player_name and player_name != ' ':
        border()
        print('Please enter a name')
        border()
        name()
    else:
        border()
        print(f'Welcome {player_name}, '
              'You have been trapped in your apartment! '
              'Zombies are attacking your city. '
              'What do you do? ')


name()


choice()
