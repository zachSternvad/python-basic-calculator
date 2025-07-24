# Entry point, main loop

#Imports
from history import History
from calculator import Calculator
from parser import Parser

# Main function
def main():
    print("Welcome to Python Calculator v1.0")
    print("Enter mathematical expressions or commands (history, clear, quit)")

    while True:
        user_input = input("Calculator > ")

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            # Visa historik (implementera senare)
            print("History feature coming soon...")
        elif user_input.lower() == "clear":
            # Rensa minne (implementera senare)
            print("Memory cleared!")
        else:
            # Matematiskt uttryck
            try:
                # Andra moduler här
                print(f"You entered: {user_input}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()