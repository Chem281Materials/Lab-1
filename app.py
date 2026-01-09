import random

BOARD_SIZE = 3
EMPTY = 0
GOAL_STATE = [1, 2, 3,
              4, 5, 6,
              7, 8, EMPTY]


def print_board(board):
    for i in range(BOARD_SIZE):
        row = board[i * BOARD_SIZE:(i + 1) * BOARD_SIZE]
        print("+---" * BOARD_SIZE + "+")
        for v in row:
            if v == EMPTY:
                print("|   ", end="")
            else:
                print(f"| {v} ", end="")
        print("|")
    print("+---" * BOARD_SIZE + "+")


def move(board, direction):
    idx = board.index(EMPTY)
    r, c = divmod(idx, BOARD_SIZE)

    if direction == "w":
        new_r, new_c = (r - 1) % BOARD_SIZE, c
    elif direction == "s":
        new_r, new_c = (r + 1) % BOARD_SIZE, c
    elif direction == "a":
        new_r, new_c = r, (c - 1) % BOARD_SIZE
    elif direction == "d":
        new_r, new_c = r, (c + 1) % BOARD_SIZE
    else:
        return False

    swap = new_r * BOARD_SIZE + new_c
    board[idx], board[swap] = board[swap], board[idx]
    return True


def is_solved(board):
    return board[-1] == GOAL_STATE[-1]


def shuffle_board(board, moves=100):
    for _ in range(moves):
        move(board, random.choice(["w", "a", "s", "d"]))


def main():
    board = GOAL_STATE.copy()
    shuffle_board(board)

    print("8-Puzzle Game")
    print("Use WASD to move tiles, q to quit.\n")

    while True:
        print_board(board)

        if is_solved(board):
            print("🎉 Puzzle solved!")
            break

        cmd = input("Move (w/a/s/d): ").strip().lower()

        if cmd == "q":
            print("Goodbye!")
            break

        if cmd not in ("w", "a", "s", "d"):
            print("Invalid input!\n")
            continue

        move(board, cmd)


if __name__ == "__main__":
    main()