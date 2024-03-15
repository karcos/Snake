from board import Board
from snake import Snake
import time
import keyboard


class App:
    """
    Main class of the Snake game. The 'run()' method, running all game.
    """
    def __init__(self):
        self.__snake = Snake()
        self.__board = Board()
        self.__interval: float = .5

    def run(self):
        """
        Main function. Running Snake game.
        :return: None.
        """
        self.__board.rand_apple(self.__snake.body)
        while True:
            if self.__board.apple_eaten(self.__snake.head_pos):
                self.__board.rand_apple(self.__snake.body)

            self.__board.show(self.__snake.body, self.__snake.head_ascii)

            if self.__win():
                print("Congratulation! You are The Winner!")
                break
            elif self.__lose():
                print(f"You lose!\nPoints: {len(self.__snake.body) - 2}")
                break

            pressed_button: str = self.__get_key()
            self.__snake.set_direction_by_button(pressed_button)
            self.__snake.move(self.__board.apple_pos)

    def __get_key(self) -> str:
        """
        Waiting 'interval' seconds to get a pressed button.
        :return: name of pressed button. Possible ['w', 'a', 's', 'd'].
        """
        button: str = str()
        start_time: time = time.time()

        while time.time() - start_time <= self.__interval:
            if keyboard.is_pressed('w'):
                button: str = 'w'
            if keyboard.is_pressed('a'):
                button: str = 'a'
            if keyboard.is_pressed('s'):
                button: str = 's'
            if keyboard.is_pressed('d'):
                button: str = 'd'

        return button

    def __lose(self) -> bool:
        """
        Checking if player lose yet.
        :return: True if player lose and False if player don't lose yet.
        """
        snake_head = self.__snake.head_pos
        if snake_head[0] not in range(10) or snake_head[1] not in range(10):
            return True
        elif snake_head in self.__snake.body[1:]:
            return True
        else:
            return False

    def __win(self):
        """
        Checking if player win yet
        :return: True if player wins and False if player don't win yet
        """
        return len(self.__snake.body) == 100
