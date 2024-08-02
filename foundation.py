
separate_text = "_________________________________________________________________________"


def log_called_method(func):
    def wrapper(*args, **kwargs):
        if args:
            print(f"{separate_text}\n"
                  f"*** called | method: {func.__name__} | class: {args[0].__class__.__name__} ***"
                  f"\n{separate_text}\n")
        else:
            print(f"{separate_text}\n"
                  f"*** called | function: {func.__name__} ***"
                  f"\n{separate_text}")
        return func(*args, **kwargs)
    return wrapper


@log_called_method
def input_data(prompts):
    """
    :param prompts: [str] or str
    :return: str
    """
    results = []
    for prompt in prompts:
        while True:
            try:
                data = input(f"\n{separate_text}\n"
                             f"{prompt}: ")
                results.append(data)
                break
            except ValueError:
                print(f"{separate_text}\n"
                      "Oops whats wrong! Try again."
                      "\n")
    return results


class Game:
    deck = {
    '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10,
        'A♠': 11,
    '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10,
        'A♥': 11,
    '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10,
        'A♦': 11,
    '2♣': 2, '3♣': 3, "4♣": 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10,
        'A♣': 11
}

    def __init__(self, round_of_game):
        self.round_of_game = round_of_game

