def create_board():
    """Создаёт игровое поле."""
    return [" " for _ in range(9)]


def print_board(board):
    """Выводит игровое поле."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def get_valid_move(board):
    """Проверяет правильность введённого номера клетки."""
    while True:
        move = input("Выберите клетку (1–9): ")

        if not move.isdigit():
            print("Ошибка! Нужно ввести число.")
            continue

        position = int(move) - 1

        if position < 0 or position > 8:
            print("Ошибка! Введите число от 1 до 9.")
            continue

        if board[position] != " ":
            print("Эта клетка уже занята!")
            continue

        return position

def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

if __name__ == "__main__":
    board = create_board()
    current_player = "X"

    for turn in range(9):
        print_board(board)

        print(f"Ход игрока {current_player}")

        position = get_valid_move(board)

        board[position] = current_player

        current_player = switch_player(current_player)

    print_board(board)