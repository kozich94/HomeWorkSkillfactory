"Привет, я понимаю что задание было сделать программку, которая за меньшее колличество попырок отгадать загаданное рандомное число от 1 - 100," \
"но мне захотелось пройти чуть дальше и попробовать выйти за рамки простого диапозона 1-100. " \
"Если принципиально нужна программка которая угадыват число от 1-100 то не проблема." \
"Так же перед запуском нахождения средних попыток угадать загаданное число, у вас спросят разрешения"


import numpy as np

low = int(input("От какого числа будем угадывать?  "))
high = int(input("И до какого числа?  "))
count = 0  # счетчик попыток
number = np.random.randint(low, high)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v2(number, low, high):
    predict = high//2
    count = 0
    print(f'Загаданное число {number}')
    while predict != number:
        predict = (low + high) // 2
        count += 1
        if predict > number:
            print(f"Загаданное число меньше {predict}")
            high = predict
        else:
            print(f"Загаданное число больше {predict}")
            low = predict
    return (count)


count = game_core_v2(number, low, high)
print(f"Число {number} отгадано за {count} попыток")

def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number, 1, 100))
    score = int(np.mean(count_ls))
    print(f"Я угадываю число в среднем за {score} попыток")
    return(score)


def ask_yes_no(score_game):
    response = None
    while response not in ("y", "n"):
        response = input("А хочешь узнать мое среднее число попыток на 1000 угаданных чисел? y-n: ").lower()
        if response == "y":
            score_game(game_core_v2)
        else:
            print("Ну ладно ¯\_(ツ)_/¯")
    return response
ask_yes_no(score_game)