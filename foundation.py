
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

    def next_round(self):
        self.round_of_game += 1


class Person:
    def __init__(self, person_name="bot", person_cash=0, person_cards=None):
        self.person_name = person_name
        self.person_cards = person_cards if person_cards is not None else {}
        self.person_cash = person_cash

    def __str__(self):
        return (f"person_name={self.person_name},"
                f" person_cash={self.person_cash} person_cards={self.person_cards}")

    @log_called_method
    def create_person(self):
        prompts = ["new_person_name", "new_person_cash"]
        get_params = input_data(prompts)

        new_person_name = get_params[0]
        try:
            new_person_cash = int(get_params[1])
        except ValueError:
            new_person_cash = 500

        newperson = Person(person_name=new_person_name, person_cash=new_person_cash)
        return newperson

    def create_bot(self, num_of_bots):
        bots_list = []
        bot_num = 1
        for i in range(num_of_bots):
            bot_default_name = f"bot{bot_num}"
            bot_default_cash = 14000
            new_bot = Person(person_name=bot_default_name, person_cash=bot_default_cash)

            bots_list.append(new_bot)
            bot_num += 1

        return bots_list
