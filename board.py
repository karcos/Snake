import random
import os
import time


class Board:
    """
    Class which is responsible for showing game board, generating new positions of apple
    and checking if apple was eaten by a snake
    """
    def __init__(self) -> None:
        self.__apple = []

    def show(self, snake_body_tab: list[list[int]], snake_head_ascii: str) -> None:
        """
        Showing game board.
        :param snake_body_tab: list of snake's parts
        :param snake_head_ascii: ascii representing head of snake
        :return:
        """
        os.system('cls')
        board = " ------------------------------\n"
        for row in range(10):
            board += '|'
            for col in range(10):
                if [row, col] in snake_body_tab:
                    if snake_body_tab[0] == [row, col]:
                        board += f" {snake_head_ascii} "
                    else:
                        board += " # "
                elif [row, col] == self.__apple:
                    board += " * "
                else:
                    board += "   "
            board += "|\n"
        board += " ------------------------------"
        print(board)

    def rand_apple(self, snake_body_tab: list[list[int]]) -> None:
        """
        Randomizing new apple's position.
        :param snake_body_tab: list of snake's parts
        :return:
        """
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
        """
        Checking if apple was eaten.
        :param snake_head_pos: Position of snake's head
        :return: True if apple was eaten and False if wasn't
        """
        if snake_head_pos == self.__apple:
            self.__apple = []
            return True
        else:
            return False

    @property
    def apple_pos(self) -> list[int]:
        """
        :return: Apple's position
        """
        return self.__apple
