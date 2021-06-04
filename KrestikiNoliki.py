EMPTY = " "
X = "X"
O = "O"
TIE = "Ничья"


def display_instruct():
    # Выводим инструкции и разметку поля
    print(
        """
    Это игра в крестики нолики.  
    Вы сможете сделать ход указав число от 0 до 8 в соотетсвии с разметкой поля:

                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    """
    )


def new_board():  # Создаем поле на котором будем играть
    board = []
    for square in range(9):  # Создаем список
        board.append(EMPTY)
    return board  # Возвращаем саму построенную


def pieces():  # Функция присваивание фишек
    player1 = X  # Присваевание фишек
    player2 = O
    print('Игрок 1 ставит: X \nИгрок 2 ставит: O')
    return player1, player2  # Возвращение значения самих фишек


def display_board(board):  # Отображение самого поля
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):  # Проверка правильности ввода хода
    moves = []
    for square in range(9):  # Проверка хода в диапозоне 0-8
        if board[square] == EMPTY:
            moves.append(square)
    return moves  # Возвращаем номер клетки хода


def winner(board):  # Определяем победителя
    WAYS_TO_WIN = ((0, 1, 2),  # Победные комбинации
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            "Если на доске имеется комбинация из трех Х или О то возвращается это же значение в виде Х или О"
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))

    return response


def player_move(board):  # Ход игрока
    legal = legal_moves(board)  # Проверка правильности хода
    move = None
    while move not in legal:  # Пока ход не будет удовлетворять условиям
        move = ask_number("Куда хотите сделать ход? (0 - 8):", 0, 9, )  # Будем запрашивать ход
        if move not in legal:
            print("\nВыбраная клетка занята \n")

    return move


def congrat_winner(the_winner):  # Вывод победителя
    if the_winner != TIE:  # Если не ничья
        print()  # Вывесли на экран победителя
    else:
        print("Ничья\n")  # В другом случае ничья
    if the_winner == X:  # В случае если победил игрок 1
        print("Выйграл игрок 1 (Х)")

    elif the_winner == O:  # В случае если победил игрок 2
        print("Выйграл игрок 2 (О)")


def next_turn(turn):  # Смена хода
    if turn == X:  # Если ходил Х
        return O  # Меняем на О
    else:
        return X  # В иных случаях меняем на X


def main():
    display_instruct()  # Сначала выводим инструкции
    player1, player2 = pieces()
    turn = player1
    board = new_board()  # Отстройка самой доски и запись ее в переменную
    display_board(board)  # Отображение построенной доски
    while not winner(board):
        if turn == player1:
            print('Ход игрока 1')
            move = player_move(board)
            board[move] = player1
            next_turn(turn)
        elif turn == player2:
            print('Ход игрока 2')
            move = player_move(board)
            board[move] = player2
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner)


main()
