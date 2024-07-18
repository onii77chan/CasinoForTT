
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
    :param prompt: str
    :return: int
    """
    while True:
        try:
            data = int(input(f"\n{separate_text}\n{prompt}"))
            return data
        except ValueError:
            print(f"{separate_text}\n"
                  "Please enter an integer."
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

    def __init__(self):
        pass


class Person:
    def __init__(self, name="bot", person_cash=0, person_cards=None):
        self.name = name
        self.person_cards = person_cards if person_cards is not None else {}
        self.person_cash = person_cash

    def __str__(self):
        return f"Person(name={self.name}, person_cards={self.person_cards})"

    @log_called_method
    def create_person(self, constructor):
        prompts = ["your_name: ", "your_cash: ",]
        results = []
        prompt_num = 0

        while True:
            try:
                results.append(input_data(prompts[prompt_num]))
            except IndexError:
                pass
            if len(results) == 2:
                person = constructor(name=results[0], person_cash=results[1])
                return person
            prompt_num += 1


constructor = Person

test = constructor().create_person(constructor)
