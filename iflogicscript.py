#!/usr/bin/env python3
def main():
    print("Welcome to the Drake Album Selector!")
    while True:
        feelings = get_feelings()
        if feelings == "quit":
            print("Thank you for using the Drake Album Selector. Goodbye!")
            break
        album = select_album(feelings)
        print("Based on your feelings, you should listen to:", album)


def get_feelings():
    print("\nHow are you feeling today?")
    print("1. Sad")
    print("2. Vengeful")
    print("3. Want Redemption")
    print("Type 'quit' to exit.")

    while True:
        try:
            choice = input("Enter the numbers corresponding to your feelings, separated by commas: ").strip()
            if choice.lower() == 'quit':
                return "quit"
            choices = [int(num) for num in choice.split(',')]
            if not all(1 <= num <= 3 for num in choices):
                raise ValueError
            return choices
        except ValueError:
            print("Invalid input. Please enter the numbers separated by commas (e.g., '1,2')")


def select_album(feelings):
    if len(feelings) == 2:
        if set(feelings) == {1, 2} or set(feelings) == {1, 3} or set(feelings) == {2, 3}:
            return "Views by Drake"
        elif set(feelings) == {1, 2} or set(feelings) == {1, 3} or set(feelings) == {2, 3}:
            return "Nothing Was The Same by Drake"
        elif set(feelings) == {1, 2} or set(feelings) == {1, 3} or set(feelings) == {2, 3}:
            return "For All The Dogs by Drake"
    elif len(feelings) == 1:
        if feelings[0] == 1:
            return "Views by Drake"
        elif feelings[0] == 2:
            return "Nothing Was The Same by Drake"
        elif feelings[0] == 3:
            return "For All The Dogs by Drake"
    else:
        return "All of Drake's albums"


if __name__ == "__main__":
    main()

