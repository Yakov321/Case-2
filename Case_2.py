# Case 2: Comet
# Developer: Tolstov Y.
#

import ru_local as ru


def main():
    '''
    Main function.
    :return: None
    '''

    speed = int(input(ru.SPEED))
    first_gravity = int(input(ru.FIRST_GRAVITY))
    second_gravity = int(input(ru.SECOND_GRAVITY))
    third_gravity = int(input(ru.THIRD_GRAVITY))
    distance = 21_320_567_980

    if first_gravity >= 16 < 26:
        speed *= 1.05
    if first_gravity > 5 <= 15:
        speed *= 0.95
    if second_gravity >= 16 < 26:
        speed *= 1.05
    if second_gravity > 5 <= 15:
        speed *= 0.95
    if third_gravity >= 16 < 26:
        speed *= 1.05
    if third_gravity > 5 <= 15:
        speed *= 0.95
    days = distance / speed
    hours = days*24
    print(f'{ru.DAYS}: {days}')
    print(f'{ru.HOURS}: {hours}')

if __name__ == '__main__':
    main()