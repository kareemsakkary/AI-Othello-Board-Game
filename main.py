import ConsoleController
import GUIController


def main():
    print("Welcome to Othello Board game!")
    print("Choose your preferred interface for the game:")
    print("1. Console")
    print("2. GUI")
    valid_input = False
    controller = None

    while not valid_input:
        preferred_choice = input(">> ")
        if preferred_choice == "1":
            controller = ConsoleController.ConsoleController()
            valid_input = True
        elif preferred_choice == "2":
            controller = GUIController.GUIController()
            valid_input = True
        else:
            print("Invalid UI choice. Please choose 1 or 2 only.")

    controller.play_game()


if __name__ == "__main__":
    main()
