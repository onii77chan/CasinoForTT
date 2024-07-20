
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
                  f"\n{separate_text}\n")
        return func(*args, **kwargs)
    return wrapper


def input_data(prompt):
    """
    :param prompt: [str] or str
    :return: str
    """
    results = []
    while True:
        try:
            data = input(f"\n{separate_text}\n"
                         f"{prompt[0]}: ")
            results.append(data)
            del prompt[0]

        except IndexError:
            return results
        except ValueError:
            print(f"{separate_text}\n"
                  "Oops whats wrong! Try again."
                  "\n")


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

    def __init__(self, round):
        self.round = round

    def next_round(self):
        self.round += 1


class Person:
    def __init__(self, person_name="bot", person_cash=0, person_cards=None):
        self.person_name = person_name
        self.person_cards = person_cards if person_cards is not None else {}
        self.person_cash = person_cash

    def __str__(self):
        return f"Person(person_name={self.person_name}, person_cash={self.person_cash} person_cards={self.person_cards})"

    @log_called_method
    def create_person(self):
        data = ["new_person_name", "new_person_cash"]

        get_params = input_data(data)
        params = [get_params[0], get_params[1]]

        newperson = Person(person_name=params[0], person_cash=params[1])

        return newperson
