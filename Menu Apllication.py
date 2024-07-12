#Creating a menu-driven application
def concatenate_strings():
    user1 = input("Enter a string: ")
    user2 = input("Enter another string: ")
    result = user1 + " " + user2
    print(result)

def convert_to_upper():
    userd = input("Enter a word: ")
    final = userd.upper()
    print(final)

def convert_to_lower():
    word = input("Enter a word: ")
    finish = word.lower()
    print(finish)

def display_menu():
    print("Menu:")
    print("1. Concatenate")
    print("2. Uppercase")
    print("3. Lowercase")
    print("4. Exit")

def main():
    while True:
        display_menu()
        direction = int(input("Select a number between (1-4): "))

        if direction == 1:
            concatenate_strings()
        elif direction == 2:
            convert_to_upper()
        elif direction == 3:
            convert_to_lower()
        elif direction == 4:
            print("Exiting the program.")
            break
        else:
            print("You have entered an invalid value.")

if __name__ == "__main__":
    main()

