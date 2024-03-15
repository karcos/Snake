class Snake:
    """
    Class which is responsible for snake object
    """
    def __init__(self) -> None:
        self.__body: list[list[int]] = [[4, 4], [4, 5]]
        self.__direction: str = "left"
        self.__direction_vector_dict: dict[str, list[int]] = {"top": [-1, 0],
                                                              "left": [0, -1],
                                                              "bottom": [1, 0],
                                                              "right": [0, 1]}
        self.__heads: dict[str, str] = {"top": '^',
                                        "left": '<',
                                        "bottom": 'v',
                                        "right": '>'}
        self.__directions_by_buttons_dict: dict[str, str] = {'w': "top",
                                                             'a': "left",
                                                             's': "bottom",
                                                             'd': "right"}
        self.__illegal_direction_changes: list[list[str]] = [["top", "bottom"], ["left", "right"]]

    def move(self, apple_pos: list[int]) -> None:
        """
        Moving snake by direction
        :param apple_pos: Apple's position
        :return:
        """
        direction_tab: list[int] = self.__direction_vector_dict[self.__direction]
        new_head: list[int] = [self.__body[0][0] + direction_tab[0], self.__body[0][1] + direction_tab[1]]

        self.__body.insert(0, new_head)

        if apple_pos != self.__body[0]:
            self.__body.pop()

    def set_direction_by_button(self, button: str) -> None:
        """
        Setting snake's direction by given button.
        :param button: Name of button. Possible ['w', 'a', 's', 'd']
        :return:
        """
        if button != "":
            check_tab = [self.__direction, self.__directions_by_buttons_dict[button]]

            for illegal_couple in self.__illegal_direction_changes:
                if set(illegal_couple).issubset(check_tab):
                    return

            self.__direction = self.__directions_by_buttons_dict[button]

    @property
    def head_ascii(self) -> str:
        """
        :return: Snake's head ascii. Possible ['^', '<', '>', 'v']
        """
        return self.__heads[self.__direction]

    @property
    def head_pos(self) -> list[int]:
        """
        :return: Snake's head position
        """
        return self.__body[0]

    @property
    def body(self) -> list[list[int]]:
        """
        :return: List of snake's parts
        """
        return self.__body



