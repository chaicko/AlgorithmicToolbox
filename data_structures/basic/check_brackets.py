# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def main():
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                print(i + 1)
                return
            b = opening_brackets_stack.pop()
            if not b.Match(next):
                print(i + 1)
                return

    # Printing answer
    try:
        b = opening_brackets_stack.pop()
        print(b.position)
    except IndexError:
        print("Success")


if __name__ == "__main__":
    main()
