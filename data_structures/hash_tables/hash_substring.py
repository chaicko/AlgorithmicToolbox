# python3
MAX_TEXT_LEN = 5 * (10 ** 5)
MAX_PATTERN_LEN = MAX_TEXT_LEN


def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    def read_input():
        return (input().rstrip(), input().rstrip())


    def print_occurrences(output):
        print(' '.join(map(str, output)))

    print_occurrences(get_occurrences(*read_input()))

