
def print_numbers():

    try: 
        file = open("numbers.txt", "r")
    except FileNotFoundError:
        print("File not found")
        exit(1)

    if not file.readable():
        print("File is not readable")
        exit(1)

    numbers = file.readline().split(",")
    for number in numbers:
        print(number)
    file.close()

if __name__ == "__main__":
    print_numbers()

