import keyboard
import time
import os
import random


def get_input(timeout: float) -> str:
    start_time: time = time.time()

    button: str = ""
    while time.time() - start_time <= timeout:

        if keyboard.is_pressed('w'):
            button: str = 'w'
        if keyboard.is_pressed('a'):
            button: str = 'a'
        if keyboard.is_pressed('s'):
            button: str = 's'
        if keyboard.is_pressed('d'):
            button: str = 'd'

        # time.sleep(0.001)  # Krótka przerwa, aby zmniejszyć użycie procesora
    return button


def get_snake_start(dir: str) -> str:
    if dir == "top":
        return '^'
    if dir == "left":
        return '<'
    if dir == "bottom":
        return 'v'
    if dir == "right":
        return '>'


def show_board(snake: list[list[int]], apple: list[int], dir: str):
    os.system('cls')
    print(" ---------- ")
    for row in range(10):
        print('|', end="")
        for col in range(10):
            if [row, col] in snake:
                if snake[0] == [row, col]:
                    print(get_snake_start(dir), end="")
                else:
                    print("#", end="")
            elif [row, col] == apple:
                print("*", end="")
            else:
                print(' ', end="")
        print('|')
    print(" ---------- ")


def get_tab_dir(dir: str) -> list[int]:
    if dir == "top":
        return [-1, 0]
    if dir == "left":
        return [0, -1]
    if dir == "bottom":
        return [1, 0]
    if dir == "right":
        return [0, 1]


def move_snake(snake: list[list[int]], dir: str, apple: list[int]):
    dir: list[int] = get_tab_dir(dir)
    snake.insert(0, [snake[0][0] + dir[0], snake[0][1] + dir[1]])

    if not apple_eaten(snake[0], apple):
        snake.pop()


def change_dir(pressed: str, dir: str) -> str:
    if pressed == 'w' and dir != "bottom":
        return "top"
    elif pressed == 'a' and dir != "right":
        return "left"
    elif pressed == 's' and dir != "top":
        return "bottom"
    elif pressed == 'd' and dir != "left":
        return "right"
    else:
        return dir


def generate_apple(snake: list[list[int]]) -> list[int]:
    possibilities = []

    for i in range(10):
        for j in range(10):
            if [i, j] not in snake:
                possibilities.append([i, j])
    try:
        return random.choice(possibilities)
    except IndexError:
        return []


def apple_eaten(snake_head: list[int], apple: list[int]) -> bool:
    if snake_head == apple:
        apple.clear()
        return True
    else:
        return False


def lose(snake: list[list[int]]):
    if snake[0][0] not in range(10) or snake[0][1] not in range(10):
        return True
    if snake[0] in snake[1:]:
        return True
    return False


def win(snake: list[list[int]]):
    return len(snake) == 100


if __name__ == '__main__':
    direction = "left"
    snake = [[4, 4], [4, 5]]

    apple = []
    while True:
        if not apple:
            apple = generate_apple(snake)
        show_board(snake, apple, direction)
        if win(snake):
            print(f"You are the Winner!")
            break
        pressed = get_input(.5)
        direction = change_dir(pressed, direction)
        move_snake(snake, direction, apple)
        if lose(snake):
            print(f"You lose!\nPoints: {len(snake) - 2}")
            break






