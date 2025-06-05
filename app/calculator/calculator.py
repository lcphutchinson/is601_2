import sys

class Calculator():
    def __init__(self) -> None:
        print("Welcome to Python REPL Calculator, v.1.2")
    def run(self) -> None:
        while True:
            user_input = input("$: ").lower().strip()
            if user_input == "exit":
                print("Thank you for using Python REPL Calculator. Exiting...")
                break
            try:
                command, x, y = user_input.split()
                #match command:
                #    case 'add':
                #        continue
                #    case 'subtract':
                #        continue
                #    case 'multiply':
                #        continue
                #    case 'divide':
                #        continue
            except ValueError:
                print("Input Error: Expected '<command> <x> <y>'")
                            
