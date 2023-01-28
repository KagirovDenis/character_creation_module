from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        damage_user = randint(3, 5)
    if char_class == 'mage':
        damage_user = randint(5, 10)
    if char_class == 'healer':
        damage_user = randint(-3, -1)
    maintext: str = ' нанёс урон противнику равный '
    return (f'{char_name} {maintext} {5 + damage_user}')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        defence_user = randint(5, 10)
    if char_class == 'mage':
        defence_user = randint(-2, 2)
    if char_class == 'healer':
        defence_user = randint(2, 5)
    return (f'{char_name} блокировал {10 + defence_user} урона')


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        special_user = 80 + 25
    if char_class == 'mage':
        special_user = 5 + 40
    if char_class == 'healer':
        special_user = 10 + 30
    return (f'{char_name} '
            f'применил специальное умение «Защита '
            f'{special_user}»')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, '
                           'Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа '
                               ).lower()
    return char_class


#if __name__ == '__main__':


def main() -> None:
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
