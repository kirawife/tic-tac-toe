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

def check_winner(board):
    winning_combinations = [
        (0, 1, 2),  # Горизонтали
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # Вертикали
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # Диагонали
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

if __name__ == "__main__":
    board = create_board()
    current_player = "X"

    for turn in range(9):
        print_board(board)

        print(f"Ход игрока {current_player}")

        position = get_valid_move(board)

        board[position] = current_player

        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Победил игрок {winner}!")
            break

        current_player = switch_player(current_player)