import random
import os
import time


class Board:
    def __init__(self) -> None:
        self.__apple = []

    def show(self, snake_body_tab: list[list[int]], snake_head_ascii: str) -> None:
        os.system('cls')
        print(" ---------- ")
        for row in range(10):
            print('|', end="")
            for col in range(10):
                if [row, col] in snake_body_tab:
                    if snake_body_tab[0] == [row, col]:
                        print(snake_head_ascii, end="")
                    else:
                        print("#", end="")
                elif [row, col] == self.__apple:
                    print("*", end="")
                else:
                    print(' ', end="")
            print('|')
        print(" ---------- ")

    def rand_apple(self, snake_body_tab: list[list[int]]) -> None:
        possibilities = []

        for row in range(10):
            for col in range(10):
                if [row, col] not in snake_body_tab:
                    possibilities.append([row, col])

        if len(possibilities) > 0:
            self.__apple = random.choice(possibilities)
        else:
            self.__apple = []

    def apple_eaten(self, snake_head_pos: list[int]) -> bool:
        if snake_head_pos == self.__apple:
            self.__apple = []
            return True
        else:
            return False

    @property
    def apple_pos(self):
        return self.__apple
