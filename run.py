"""
This is a survival game taking place in a zombie outbreak
YOU MUST SURVIVE!
"""
weapons = []
knowledge = []
bag = []


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
            weapons.append('knife')
            knife()
        elif action == 'b':
            weapons.append('bat')
            bat()
        else:
            print('invalid choice, try again')
            weapon()
    else:
        print('invalid choice, try again')
        weapon()


def knife():
    """
    If the user pressed "a" to take knife in weapon
    they will be brought here.
    """
    print('Armed with the biggest knife you could find '
          'you are ready to face what is outside. ')
    leave()


def bat():
    """
    If the user pressed "b" to take baseball bat in weapon
    they will be brought here.
    """
    print('Armed with your trusty bat '
          'you are ready to face what is outside. ')
    leave()


def leave():
    """
    If the user pressed "b" to leave apartment in choice_a
    they will be brought here.
    """
    print('You decide that you have no time to waste. '
          'As you open the door to the hallway, you can hear screams and car '
          'alarms trying to compete for your attention. '
          'You look around and see blood and body parts everywhere '
          'But no zombies! You wonder which is the safest route to take. ')

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
    If the user pressed "a" to take stairs in leave
    they will be brought here.
    """
    print('As you are running down the stairs you can hear strange growling '
          'from the bottom ')

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
            choice_b()
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
    If the user pressed "a" to take stairs down in stairs
    they will be brought here.
    """
    print('As you continue down the stairs you see two zombies '
          'eating someone right next to the door to the exit. ')

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
    If the user pressed "a" to sneak in stairs_down
    they will be brought here.
    """
    print('You successfully sneak past the zombies and avoid '
          'stepping into any pool of blood. As you open the door '
          'you are greeted by a city in complete chaos. '
          'You know the odds are against you but atleast you got a chance! '
          'Congratulations you survived chapter one! ')


def run():
    """
    If the user pressed "b" to run in stairs_down
    they will be brought here.
    """
    print('As you sprint towards the exit '
          'you slip on a pool of blood '
          'and fall on your back hitting your head. '
          'As you try to collect yourself, your vision returns '
          'to normal only in time to see one of the zombies '
          'quickly approaching your face with an open maw. '
          'You have died! GAME OVER! ')
    name()
    choice()


def attack():
    """
    If the user pressed "c" to attack them in stairs_down
    they will be brought here.
    """
    if 'knife' in weapons:
        weapons.pop()
        print('You pull out your knife and stab the closest zombie. '
              'It does not seem to affect them. '
              'They both rise up and start attacking you as you '
              'repeatedly stab them, fighting for your life. '
              'They overwhelm you. You have died! GAME OVER! ')
    elif 'knife' in weapons and 'tv' in knowledge:
        print('As you approach the zombies you remember what you '
              'heard in the news and aim for the first zombies '
              'head. Killing it in one blow! You quickly pull out '
              'your knife and stab the other one right through its eyes. '
              'Standing in disbelief of what you have done, you feel '
              'that you are now ready to face the grim reality of the world. '
              'Congratulations you survived chapter one! ')
    elif 'bat' in weapons:
        weapons.pop()
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
        name()
        choice()
    elif 'bat' in weapons and 'tv' in knowledge:
        print('As you prepare to attack the zombies you'
              'remember what they said on the news. '
              'You yell at the zombies and start to approach you. '
              'As the first one comes close enough you aim for the head. '
              'A loud cracking sound comes from the zombie as it falls down. '
              'You quickly move towards the other one and hit it on its head. '
              'It too falls down and you start to repeatedly bash its head '
              'until it is cracked. You then move to the first zombie to '
              'finish the job. '
              'You take a deep breath, covered in blood and knowledge '
              'you are ready to face what awaits you outside. '
              'Congratulations you survived chapter one! ')
    else:
        print('You engange the zombies in hand to hand combat '
              'it is a futile attempt as they quickly start biting you. '
              'You have died! GAME OVER! ')
        name()
        choice()


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
    if 'bat' in weapons:
        weapons.pop()
        print('You quickly use your bat and put it in the door handle '
              'thus preventing it from being open. '
              'You are now trapped on the roof, with no supplies '
              'or a way out. You starve to death. '
              'You have died! GAME OVER! ')
        name()
        choice()
    elif 'bat' in weapons and 'supplies' in bag:
        weapons.pop()
        bag.pop()
        print('You quickly use your bat and put it in the door handle '
              'thus preventing it from being open. '
              'With no way out you have no choice but to wait '
              'for rescue. You ration your supplies and '
              'manage to live long enough for a helicopter to spot you. '
              'Congratulations you survived chapter one! ')
    else:
        print('All you can do is hold the opposite end of the door. '
              'The zombies overpower you and you have nowhere to go. '
              'You decide its better to jump to your death than to be '
              'eaten alive. You have died! GAME OVER! ')
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
          'inside! They grab you before you can react '
          'You have been eaten! GAME OVER!')
    name()
    choice()


def choice_b():
    """
    If the user pressed "b" to stay on choice they will be brought here.
    """
    print('You have chosen to stay in your apartment. '
          'You can turn on the tv to see the news '
          'or you could look at your phone to see if anyone has called you.')

    action = input('Press "a" to turn on the tv or "b" to look at your phone: '
                   '')
    if action != ' ':
        if action == 'a':
            knowledge.append('kill')
            watch_tv()
        elif action == 'b':
            print('phone')
        else:
            print('invalid choice, try again')
            choice_b()
    else:
        print('invalid choice, try again')
        choice_b()


def watch_tv():
    """
    If the user pressed "a" to watch tv on choice_b
    they will be brought here.
    """
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

    action = input('Press "a" to check on your phone '
                   '"b" to gather as much water as you can '
                   '"c" to gather your supplies: ')
    if action != ' ':
        if action == 'a':
            print('phone')
        elif action == 'b':
            print('water')
        elif action == 'c':
            print('supplies')
        else:
            print('invalid choice, try again')
            watch_tv()
    else:
        print('invalid choice, try again')
        watch_tv()


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
