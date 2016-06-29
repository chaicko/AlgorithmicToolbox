# python3
import random

MAX_TEXT_LEN = 5 * (10 ** 5)
MAX_PATTERN_LEN = MAX_TEXT_LEN


def poly_hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans


def precompute_hashes(text, pattern, p, x):
    hashes = [0] * (len(text) - len(pattern) + 1)
    substr = text[len(text)-len(pattern):len(text)]
    hashes[len(text)-len(pattern)] = poly_hash(substr, p, x)
    y = 1
    for i in range(1, len(pattern)+1):
        y = (y * x) % p
    for i in reversed(range(len(text)-len(pattern))):
        a = (x * hashes[i+1]) % p
        b = ord(text[i]) % p
        c = (y * ord(text[i+len(pattern)])) % p
        hashes[i] = (a + b - c) % p
    return hashes


def rabin_karp(pattern, text):
    p = 10000007
    x = random.randint(1, p - 1)
    res = []
    pattern_hash = poly_hash(pattern, p, x)
    h = precompute_hashes(text, pattern, p, x)
    for i in range(len(text)-len(pattern)+1):
        if pattern_hash != h[i]:
            continue

        if pattern == text[i:i+len(pattern)]:
            res.append(i)
    return res


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

    print_occurrences(rabin_karp(*read_input()))

