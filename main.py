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