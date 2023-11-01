
import sys   

def state():

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

    if len(sys.argv) < 2:
        exit(1)

    city = sys.argv[1]

    cities = capital_cities.values()

    if city not in cities:
        print("Unknown city")
        exit(1)

    prefixes = [k for k, v in capital_cities.items() if v == city]

    if len(prefixes) == 0 or len(prefixes) > 1:
        print("Unknown city")
        exit(1)

    state_names = [k for k, v in states.items() if v == prefixes[0]]
    if len(state_names) == 0 or len(state_names) > 1:
        print("Unknown state")
        exit(1)

    print(state_names[0])



if __name__ == '__main__':
    state()
