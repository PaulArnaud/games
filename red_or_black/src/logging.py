from termcolor import colored


class Logger:
    @staticmethod
    def print_game_info(message: str) -> None:
        print(colored(message, "blue", "on_yellow"))

    @staticmethod
    def print_game_question(message: str) -> None:
        print(colored(message, "green", "on_light_magenta"))

    @staticmethod
    def print_game_order(message: str) -> None:
        print(colored(message, "white", "on_light_red"))
