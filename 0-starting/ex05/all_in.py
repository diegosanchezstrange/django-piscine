import sys


def all_in():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }


    if len(sys.argv) < 2 or len(sys.argv) > 2:
        exit(1)

    args = sys.argv[1].split(',')

    for arg in args:
        arg = arg.strip().title()
        if len(arg) == 0:
            continue
        if arg in states:
            print(arg, "has", capital_cities[states[arg]], "as its capital")
        elif arg in capital_cities.values():
            prefixes = [k for k, v in capital_cities.items() if v == arg]

            if len(prefixes) == 0 or len(prefixes) > 1:
                print("Unknown city")
                exit(1)

            state_names = [k for k, v in states.items() if v == prefixes[0]]
            if len(state_names) == 0 or len(state_names) > 1:
                print("Unknown state")
                exit(1)

            print(arg, "is the capital of", state_names[0])
        else:
            print(arg, "is neither a capital city nor a state")


if __name__ == '__main__':
    all_in()
