# python3

def read_input():
    i_or_f = input()
    if 'F' in i_or_f:
        path = input()
        path = "tests/" + path
        with open(path, "r") as f:
            pattern = f.readline()
            text = f.readline()
    if 'I' in i_or_f:
        pattern = input()
        text = input()
    return (pattern.rstrip(), text.rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_hash(string):
    number_of_characters = 256
    prime_number = 89 #could be any other prime number
    length_of_string = len(string)
    hash = 0
    for i in range(length_of_string):
        hash = (prime_number * hash + ord(string[i])) % number_of_characters
    return hash

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    length_of_text = len(text)
    length_of_pattern = len(pattern)
    occurances = []
    for i in range(length_of_text-length_of_pattern%length_of_pattern):
        if get_hash(text[i: i + length_of_pattern]) == get_hash(pattern):
            for j in range(length_of_pattern):
                if text[i+j] != pattern[j]:
                    break
            if j==length_of_pattern-1:
                occurances.append(i)
    return occurances

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
