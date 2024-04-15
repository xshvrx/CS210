# Write a program that reads words from a filename, which is given as a string argument. It should return the words from the file in a list, sorted in reverse alphabetical order (case insensitive) .

# For instance, if the file has

# bell tea  Zebra
# apple
# yellow
# Then the output should be

# ['Zebra', 'yellow', 'tea', 'bell', 'apple']

def reverse_sorted_words(filename):

    try:
        with open(filename, 'r') as file:
            # Reads the file and split it into words
            words = file.read().split()
            # Sort the words in reverse alphabetical order
            reversed_words = sorted(words, key=lambda word: word.lower(), reverse=True)
            return reversed_words
    except FileNotFoundError:
        print("File not found.")
        return []
